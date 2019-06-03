#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <signal.h>


#include "QueryProtocol.h"
#include "MovieSet.h"
#include "MovieIndex.h"
#include "DocIdMap.h"
#include "htll/Hashtable.h"
#include "QueryProcessor.h"
#include "FileParser.h"
#include "FileCrawler.h"

DocIdMap docs;
Index docIndex;

#define BUFFER_SIZE 1000
#define SEARCH_RESULT_LENGTH 1500
char movieSearchResult[SEARCH_RESULT_LENGTH];

int Cleanup();

void sigint_handler(int sig) {
  write(0, "Exit signal sent. Cleaning up...\n", 34);
  Cleanup();
  exit(0);
}


void Setup(char *dir) {
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
    printf("Please enter the correct number of arguments.\n");
    return -1;
  }
  char *dir_to_crawl = (char *) argv[1];
  int port_num = atoi(argv[2]);

  // Setup graceful exit
  struct sigaction kill;

  kill.sa_handler = sigint_handler;
  kill.sa_flags = 0;  // or SA_RESTART
  sigemptyset(&kill.sa_mask);

  if (sigaction(SIGINT, &kill, NULL) == -1) {
    perror("sigaction");
    exit(1);
  }

  Setup(dir_to_crawl);
  // Step 1: get address/port info to open

  // Step 2: Open socket
  // create the server socket
  int server_socket;
  if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
    printf("\n Error : Could not create server socket \n");
    return -1;
  }
  // define the server address
  struct sockaddr_in server_address;
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(port_num);
  server_address.sin_addr.s_addr = INADDR_ANY;

  // Step 3: Bind socket
  // bind the socket to our specified IP and port
  bind(server_socket, (struct sockaddr *) &server_address,
  sizeof(server_address));

  // Step 4: Listen on the socket


  if (listen(server_socket, 5) < 0) {  // how many clients we are listening
    printf("Fialed to listen\n");
    return -1;
  }
  // Step 5: Handle clients that connect
  // SearchResult result = (SearchResult)malloc(sizeof(SearchResult));
  while (1) {
    printf("Waiting for connection...\n");
    int client_socket;
    client_socket = accept(server_socket, NULL, NULL);
    printf("Client Connected%d\n", client_socket);

    // sending ack
    int sendack;
    if ((sendack = SendAck(client_socket)) < 0) {
      printf("Server sending ACK failed.\n");
      return -1;
    } else {
      printf("Server sent ack\n");
    }

    char buffer[1000];
    int len = read(client_socket, buffer, sizeof(buffer) - 1);
    buffer[len] = '\0';
    sleep(3);

    SearchResultIter iter = FindMovies(docIndex, buffer);
    if (iter == NULL) {
      snprintf(movieSearchResult, SEARCH_RESULT_LENGTH, "No Result Found.");
      write(client_socket, movieSearchResult, strlen(movieSearchResult));
      continue;
    }
    printf("num_responses: %d\n", NumResultsInIter(iter));
    char numBuff[BUFFER_SIZE];
    snprintf(numBuff, BUFFER_SIZE, "%d", NumResultsInIter(iter));
    write(client_socket, numBuff, strlen(numBuff));


    // read(client_socket, movieSearchResult, sizeof(movieSearchResult));

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

  // Step 6: Close the socket

  // Got Kill signal


  close(server_socket);

  Cleanup();

  return 0;
}
