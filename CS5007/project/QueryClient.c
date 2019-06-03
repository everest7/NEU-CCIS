#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <arpa/inet.h>

#include "includes/QueryProtocol.h"
#include "QueryClient.h"

/*
Name: Weisong Chen
Date: Apr 19
*/

char *port_string = "1500";
unsigned short int port;
char *ip = "127.0.0.1";

#define BUFFER_SIZE 1000

void RunQuery(char *query) {
  // Find the address

  // Create the socket
  // One side of connection
  int socketfd;
  if ((socketfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
    printf("\n Error : Could not create socket \n");
    return;
  }
  // specify an address for the socket
  struct sockaddr_in server_address;
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(port);
  server_address.sin_addr.s_addr = INADDR_ANY;
  // Connect to the server
  int connect_status = connect(socketfd, (struct sockaddr *)
  &server_address, sizeof(server_address));
  if (connect_status < 0) {
    printf("\nConnection Failed\n");
    return;
  }
  // send term to server
  // int server_socket;
  // server_socket = accept(socketfd, NULL, NULL);
  char recvBuff[BUFFER_SIZE];
  int len;
  if ((len = read(socketfd, recvBuff, sizeof(recvBuff) - 1)) < 0) {
    printf("Read recvBuff failed\n");
  }
  recvBuff[len] = '\0';
  if (CheckAck(recvBuff) < 0) {
    printf("Get Response Num. Check ack failed on client side.\n");
  } else {
    printf("Connected to movie server\n");
  }
  char termBuffer[BUFFER_SIZE];
  // strcpy(termBuffer, query);
  snprintf(termBuffer, BUFFER_SIZE, "%s", query);
  write(socketfd, termBuffer, strlen(termBuffer));

  // sending ack
  // int sendack;
  // if ((sendack = SendAck(socketfd)) < 0) {
  //   printf("Server sending ACK failed.\n");
  //   return;
  // }
  // Adding checkack

  if ((len = read(socketfd, recvBuff, sizeof(recvBuff) - 1)) < 0) {
    printf("read number of responses failed\n");
  }
  recvBuff[len] = '\0';
  if (strcmp(recvBuff, "No Result Found.") == 0) {
    printf("%s\n", recvBuff);
    close(socketfd);
    return;
  }
  int numResponse = atoi(recvBuff);
  // recvBuff[0] = '\0';
  int i;
  for (i = 0; i < numResponse; i++) {
    int sendack;
    if ((sendack = SendAck(socketfd)) < 0) {
      printf("Client send ack failed\n");
      return;
    }
    if ((len = read(socketfd, recvBuff, sizeof(recvBuff) - 1)) < 0) {
      printf("read movie entry failed\n");
    }
    recvBuff[len] = '\0';
    printf("%s\n", recvBuff);
    // fputs(recvBuff, stdout);
    // recvBuff[0] = '\0';
  }
  if ((SendAck(socketfd)) < 0) {
    printf("Client send ack failed\n");
    return;
  }
  if ((len = read(socketfd, recvBuff, sizeof(recvBuff) - 1)) < 0) {
    printf("read movie entry failed\n");
  }
  recvBuff[len] = '\0';
  if (CheckGoodbye(recvBuff) < 0) {
    printf("CheckGoodbye Failed\n");
  }
  close(socketfd);
}

void RunPrompt() {
  char input[BUFFER_SIZE];

  while (1) {
    printf("Enter a term to search for, or q to quit: ");
    scanf("%s", input);

    printf("input was: %s\n", input);

    if (strlen(input) == 1) {
      if (input[0] == 'q') {
        printf("Thanks for playing! \n");
        return;
      }
    }
    printf("\n\n");
    RunQuery(input);
  }
}

int main(int argc, char **argv) {
  // Check/get arguments
  if (argc < 0 || argc != 3) {
    perror("Error");
    return 0;
  } else {
    ip = argv[1];
    port = atoi(argv[2]);
  }
  if (strcmp(ip, "localhost") != 0) {
    int first, second, third, fourth;
    sscanf(ip, "%d.%d.%d.%d", &first, &second, &third, &fourth);
    if (0 <= first && first <= 255 && 0 <= second && second <= 255
    && 0 <= third && third <= 255 && 0 <= fourth &&
        fourth <= 255) {
      RunPrompt();
    } else {
      printf("Please enter the correct IP address\n");
      return 0;
    }
  } else {
    RunPrompt();
    return 0;
  }
  // Get info from user
}
