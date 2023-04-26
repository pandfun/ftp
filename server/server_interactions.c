#include "../core/core.h"



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

	int i = 1;
	while (i-- > 0) {

		rc = recv(client_socket, buffer, BUFFSIZE, 0);
		if (rc < 0)
			err("recv");


		if (!strcmp(buffer, "exit")) {
			return;

		} else {
			memset(buffer, 0, strlen(buffer) * sizeof(char));
			continue;
			
		}
	}

	return;
}