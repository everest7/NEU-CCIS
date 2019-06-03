#ifndef QUERYPROTOCOL_H
#define QUERYPROTOCOL_H

extern const char *ACK;

extern const char *GOODBYE;

extern const char *KILL; 

/**
 * Sends an ACK (acknowledgement) packet to the 
 * recipient. 
 *
 * INPUT: int for the socket file descriptor. 
 * 
 * RETURNS: 0 if successfully sends. 
 *          -1 if there is an error. 
 */
int SendAck(int socket_fd);

/**
 * Checks if a provided response (string) is 
 * actually an ACK signal. 
 *
 *  INPUT: A pointer to the response/buffer recieved. 
 * 
 * RETURNS: 0 if response is an ACK
 *          -1 otherwise
 */
int CheckAck(char *response);

/**
 * Sends a GOODBYE packet to the recipient. 
 *
 * INPUT: int for the file descriptor to send the GOODBYE to. 
 * 
 * RETURNS: 0 if successfully sends. 
 *         -1 if there is an error. 
 */
int SendGoodbye(int socket_fd);

/**
 * Checks to see if a given response is a GOODBYE
 *  or not. 
 *
 * RETURNS: 0 if response is a GOODBYE. 
 *         -1 otherwise. 
 *
 */
int CheckGoodbye(char *response);

/**
 *  Sends a KILL packet to the recipient. 
 *
 *  INPUT: file descriptor that is the recipient of a KILL msg. 
 *
 */
int SendKill(int socket_fd);

/**
 * Checks if a given response is a KILL message.
 *
 * INPUT: string (presumably a message)
 *
 * RETURNS: 0 if response is a KILL
 *         -1 otherwise. 
 *
 */
int CheckKill(char *response); 



#endif // QUERYPROTOCOL_H
