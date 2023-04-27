#include "../core/core.h"
#include "server.h"



/*
 * Function handles interactions with the client.
 * 
 * This is in sync with the "../client/client_interactions.c"
 * Any changes made here should be reflected there as well if needed.
 */
void server_interactions(int client_socket)
{
	int rc;
	char buffer[BUFFSIZE];
	memset(buffer, 0, sizeof(char) * BUFFSIZE);


	while (1) {

		rc = recv(client_socket, buffer, BUFFSIZE, 0);
		if (rc < 0)
			err("recv");


		if (!strcmp(buffer, "exit")) {
			return;

		} else if (!strcmp(buffer, "ls")) {

			list_dir(client_socket, 0);
			memset(buffer, 0, strlen(buffer));
			continue;

		} else if (!strcmp(buffer, "ls -a")) {

			list_dir(client_socket, 1);
			memset(buffer, 0, strlen(buffer));
			continue;

		} else if (!strcmp(buffer, "read")) {

			send_file(client_socket);
			memset(buffer, 0, strlen(buffer));
			continue;

		}
		
		
		else {

			memset(buffer, 0, strlen(buffer) * sizeof(char));
			continue;
			
		}
	}

	return;
}