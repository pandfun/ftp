#include "../core/core.h"
#include "client.h"



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

	clock_t time;


	while (1) {

		printf(">> ");
		fgets(buffer, BUFFSIZE, stdin);
		buffer[strcspn(buffer, "\n")] = 0;

		
		if (!strcmp(buffer, "exit")) {
			
			printf("Connection terminating...\n");
			rc = send(server_socket, buffer, strlen(buffer)+1, 0);
			if (rc < 0)
				err("rc");

			return;

		} else if (!strcmp(buffer, "ls")) {
			
			rc = send(server_socket, buffer, strlen(buffer)+1, 0);
			if (rc < 0)
				err("send");

			memset(buffer, 0, strlen(buffer));
			recv(server_socket, buffer, BUFFSIZE, 0);
			
			printf("%s", buffer);
			
			memset(buffer, 0, strlen(buffer));
			continue;

		} else if (!strcmp(buffer, "ls -a")) {

			rc = send(server_socket, buffer, strlen(buffer)+1, 0);
			if (rc < 0)
				err("send");

			memset(buffer, 0, strlen(buffer));			
			recv(server_socket, buffer, BUFFSIZE, 0);

			printf("%s", buffer);

			memset(buffer, 0, strlen(buffer));
			continue;

		} else if (!strcmp(buffer, "read")) {

			rc = send(server_socket, buffer, strlen(buffer)+1, 0);
			if (rc < 0)
				err("send");
			
			memset(buffer, 0, strlen(buffer));

			printf("Enter the file you want to read: ");
			fgets(buffer, 20 * sizeof(char), stdin);
			buffer[strcspn(buffer, "\n")] = 0;
			
			rc = send(server_socket, buffer, strlen(buffer)+1, 0);
			if (rc < 0)
				err("send");
			
			time = clock();
			rc = recv(server_socket, file_buffer, FILEBUFF, 0);
			time = clock() - time;

			if (rc < 0)
				err("recv");
			
			printf("FILE CONTENTS:\n\n%s\n\n", file_buffer);
			display_speed(time, strlen(file_buffer)+1);

			memset(file_buffer, 0, strlen(file_buffer));
			memset(buffer, 0, strlen(buffer));
			continue;

		}
		
		
		else {

			printf("%s: command not found\n");
			
			memset(buffer, 0, strlen(buffer) * sizeof(char));
			continue;
			
		}

		send(server_socket, buffer, strlen(buffer)+1, 0);
		memset(buffer, 0, strlen(buffer) * sizeof(char));
	}
}

void display_speed(clock_t t, int len)
{
	double cpu_time = (double) t / CLOCKS_PER_SEC;
	double kb_ps = (len / cpu_time) / (1024 * 1024);

	printf("Fetched %d bytes in %lf seconds (%lf kB/sec)\n\n", 
		len, cpu_time, kb_ps);
	
	return;
}