#include "../core/core.h"
#include "../secrets/secrets.h"

/* 
 * Function called by client to connect to the server
 */
int connect_client(int port_no)
{
	int client_socket;
	struct sockaddr_in server_addr;
	socklen_t addr_size;
	int rc;

	client_socket = socket(PF_INET, SOCK_STREAM, 0);
	if (client_socket < 0) {
		perror("socket");
		exit(1);
	}

	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(port_no);

	// destination IP
	server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
	
	memset(server_addr.sin_zero, 0, sizeof server_addr.sin_zero);

	addr_size = sizeof server_addr;
	rc = connect(client_socket, (struct sockaddr *) &server_addr, addr_size);
	if (rc < 0) {
		perror("connect");
		exit(1);
	} else {
		printf("Connected to the server!\n");
	}

	return client_socket;
}