#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include <signal.h>
#include <errno.h>

#include "QueryProtocol.h"
#include "MovieSet.h"
#include "MovieIndex.h"
#include "DocIdMap.h"
#include "htll/Hashtable.h"
#include "QueryProcessor.h"
#include "FileParser.h"
#include "FileCrawler.h"

/*
Name: Weisong Chen
Date: Apr 19
*/

#define BUFFER_SIZE 1000

int Cleanup();

DocIdMap docs;
Index docIndex;

#define SEARCH_RESULT_LENGTH 1500

char movieSearchResult[SEARCH_RESULT_LENGTH];

void sigchld_handler(int s) {
  write(0, "Handling zombies...\n", 20);
  // waitpid() might overwrite errno, so we save and restore it:
  int saved_errno = errno;

  while (waitpid(-1, NULL, WNOHANG) > 0);

  errno = saved_errno;
}

void sigint_handler(int sig) {
  write(0, "Ahhh! SIGINT!\n", 14);
  Cleanup();
  exit(0);
}

/**
 *
 */
int HandleConnections(int sock_fd) {
  // Step 5: Accept connection
  // Fork on every connection.
  pid_t childpid;
  int client_socket = accept(sock_fd, NULL, NULL);

  if (client_socket < 0) {
    // printf("Error in accepting\n");
    close(sock_fd);
    Cleanup();
    exit(1);
  }
  printf("Client Connected \n");
  // Fork on every connection.

  if ((childpid = fork()) == 0) {  // child process
    close(sock_fd);
    sleep(3);
    int sendack;
    if ((sendack = SendAck(client_socket)) < 0) {
      printf("Server sending ACK failed.\n");
      return -1;
    }

    char buffer[1000];
    int len = read(client_socket, buffer, sizeof(buffer) - 1);
    buffer[len] = '\0';

    SearchResultIter iter = FindMovies(docIndex, buffer);
    if (iter == NULL) {
      // strcpy(movieSearchResult, "No Result Found.");
      snprintf(movieSearchResult, SEARCH_RESULT_LENGTH,
      "No Result Found.");
      write(client_socket, movieSearchResult, strlen(movieSearchResult));
      if (SendGoodbye(client_socket) < 0) {
        printf("SendGoodbye failed\n");
      }
      return -2;
    }
    printf("num_responses: %d\n", NumResultsInIter(iter));
    char numBuff[BUFFER_SIZE];
    snprintf(numBuff, BUFFER_SIZE, "%d", NumResultsInIter(iter));
    write(client_socket, numBuff, strlen(numBuff));

    while (SearchResultIterHasMore(iter)) {
      len = read(client_socket, movieSearchResult,
      sizeof(movieSearchResult) - 1);
      movieSearchResult[len] = '\0';
      if (CheckAck(movieSearchResult) < 0) {
        printf("Check one piece of result failed\n");
        return -1;
      }
      SearchResult result = (SearchResult) malloc(sizeof(*result));
      result->doc_id = -1;
      result->row_id = -1;
      SearchResultGet(iter, result);
      CopyRowFromFile(result, docs, movieSearchResult);
      write(client_socket, movieSearchResult, strlen(movieSearchResult));

      SearchResultNext(iter);
      free(result);
    }

    len = read(client_socket, movieSearchResult, sizeof(movieSearchResult) - 1);
    movieSearchResult[len] = '\0';
    if (CheckAck(movieSearchResult) == -1) {
      printf("Check one piece of result failed\n");
      return -1;
    }
    SearchResult result = (SearchResult) malloc(sizeof(*result));
    result->doc_id = -1;
    result->row_id = -1;
    SearchResultGet(iter, result);
    CopyRowFromFile(result, docs, movieSearchResult);
    write(client_socket, movieSearchResult, strlen(movieSearchResult));
    free(result);
    DestroySearchResultIter(iter);

    len = read(client_socket, movieSearchResult, sizeof(movieSearchResult) - 1);
    movieSearchResult[len] = '\0';
    if (CheckAck(movieSearchResult) == -1) {
      printf("Check one piece of result failed\n");
      return -1;
    }
    if (SendGoodbye(client_socket) < 0) {
      printf("SendGoodbye failed\n");
    }
  }
  return 0;
}

void Setup(char *dir) {
  struct sigaction sa;

  sa.sa_handler = sigchld_handler;  // reap all dead processes
  sigemptyset(&sa.sa_mask);
  sa.sa_flags = SA_RESTART;
  if (sigaction(SIGCHLD, &sa, NULL) == -1) {
    perror("sigaction");
    exit(1);
  }

  struct sigaction kill;

  kill.sa_handler = sigint_handler;
  kill.sa_flags = 0;  // or SA_RESTART
  sigemptyset(&kill.sa_mask);

  if (sigaction(SIGINT, &kill, NULL) == -1) {
    perror("sigaction");
    exit(1);
  }

  printf("Crawling directory tree starting at: %s\n", dir);
  // Create a DocIdMap
  docs = CreateDocIdMap();
  CrawlFilesToMap(dir, docs);
  printf("Crawled %d files.\n", NumElemsInHashtable(docs));

  // Create the index
  docIndex = CreateIndex();

  // Index the files
  printf("Parsing and indexing files...\n");
  ParseTheFiles(docs, docIndex);
  printf("%d entries in the index.\n", NumElemsInHashtable(docIndex->ht));
}

int Cleanup() {
  DestroyOffsetIndex(docIndex);
  DestroyDocIdMap(docs);
  return 0;
}

int main(int argc, char **argv) {
  // Get args
  if (argc < 1) {
    printf("Please enter the correct arguments\n");
    exit(1);
  }
  char *dir_to_crawl = (char *) argv[1];
  int port_num = atoi(argv[2]);

  Setup(dir_to_crawl);

  // declare necessary variables

  int sock_fd, ret;

  // int client_socket;
  // struct sockaddr_in acceptAddr;

  // socklen_t addr_size;

  // char buffer[1024];
  // Step 1: Get address stuff
  // int s;
  struct addrinfo hints;
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_family = AF_INET;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_flags = AI_PASSIVE;
  // s = getaddrinfo(NULL, "1234", &hints, &result);
  // Step 2: Open socket
  if ((sock_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
    printf("\n Error : Could not create server socket \n");
    exit(1);
  }
  struct sockaddr_in server_address;
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(port_num);
  server_address.sin_addr.s_addr = INADDR_ANY;

  // Step 3: Bind socket
  if ((ret = bind(sock_fd, (struct sockaddr *) &server_address,
  sizeof(server_address))) < 0) {
    printf("Error in binding\n");
    exit(1);
  }
  // Step 4: Listen on the socket


  if (listen(sock_fd, 5) < 0) {  // how many clients we are listening
    printf("Fialed to listen\n");
    exit(1);
  }
  // Step 5: Handle the connections
  while (1) {
    int handle = HandleConnections(sock_fd);
    if (handle == -2) {
      printf("TERM NOT FOUND\n");
      continue;
    }
  }
  // Got Kill signal
  printf("\n\nCleaning the index\n");
  close(sock_fd);
  Cleanup();
  return 0;
}
