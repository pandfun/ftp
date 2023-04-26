#include "../core/core.h"
#include <time.h>

// Numbers of connections the server can handle
#define NUM_OF_CONNECTIONS 1

/* 
 * Function called by server to connnect to the clients! 
 */
int connect_server(int port_no)
{
	int welcome_socket, new_socket;
	struct sockaddr_in server_addr;
	struct sockaddr_storage server_storage;
	socklen_t addr_size;
	time_t t;

	int rc;

	welcome_socket = socket(PF_INET, SOCK_STREAM, 0);
	if (welcome_socket < 0) {
		perror("socket");
		exit(1);
	}

	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(port_no);
	
	// IP of the source's destination
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);

	memset(server_addr.sin_zero, 0, sizeof server_addr.sin_zero);
	
	addr_size = sizeof server_addr;

	rc = bind(welcome_socket, (struct sockaddr *) &server_addr, addr_size);
	if (rc < 0) {
		perror("bind");
		exit(1);
	}

	rc = listen(welcome_socket, 1);
	if (rc < 0) {
		perror("listen");
		exit(1);
	} else {
		printf("Listening...\n");
	}

	addr_size = sizeof server_storage;
	new_socket = accept(welcome_socket, (struct sockaddr *) &server_storage,
		&addr_size);
	time(&t);
	
	if (new_socket < 0) {
		perror("accept");
		exit(1);
	} else {
		
		rc = getpeername(new_socket, 
		(struct sockaddr *) &server_addr, &addr_size);
		printf("Connected to client: %s on %s", 
			inet_ntoa(server_addr.sin_addr), ctime(&t));
	}

	return new_socket;
}