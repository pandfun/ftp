#include "../core/core.h"



/*
 * Function handles interactions with the server.
 * 
 * This is in sync with "../server/server_interactions.c"
 * Any changes made here should be reflected there as well if needed.
 */
void client_interactions(int server_socket)
{
	int rc;

	char buffer[BUFFSIZE];
	char file_buffer[FILEBUFF];


	while (1) {

		printf(">> ");
		fgets(buffer, BUFFSIZE, stdin);
		buffer[strcspn(buffer, "\n")] = 0;

		
		if (!strcmp(buffer, "exit")) {
			printf("Connection terminating...\n");
			send(server_socket, buffer, strlen(buffer)+1, 0);
			return;

		} else {
			printf("%s: command not found\n");
			memset(buffer, 0, strlen(buffer) * sizeof(char));
			continue;
			
		}

		send(server_socket, buffer, strlen(buffer)+1, 0);
		memset(buffer, 0, strlen(buffer) * sizeof(char));
	}
}