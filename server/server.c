#include "../core/core.h"
#include "server.h"

int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("Incorrect usage!\n%s <port_no>\n", argv[0]);
		exit(1);
	}

	int port_no = atoi(argv[1]);
	int client_socket = connect_server(port_no);

	server_interactions(client_socket);

	return 0;
}

