#include "../core/core.h"
#include "client.h"

int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("Wrong usage!\n%s <port_no>\n", argv[0]);
		return -1;
	}

	int port_no = atoi(argv[1]);
	int server_socket = connect_client(port_no);

	client_interactions(server_socket);

	return 0;
}