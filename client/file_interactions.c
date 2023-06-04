#include "../core/core.h"
#include "client.h"


/* 
 * Function to handle receiving files from the server
 * It will either just display the file contents
 * or it can be saved on the client machine based on the arguments
 * 
 * Flag Transalation
 * 0 -> read (just print the contents)
 * 1 -> get (save the file contents with the same filename on client)
 */
void recv_file(int socket, int flag)
{
	int rc;
	char file_buffer[FILEBUFF] = {0};
	char buffer[BUFFSIZE] = {0};

	clock_t time;

	if (!flag)
		printf("Enter the file you want to read: ");
	else
		printf("Enter the file you want to get: ");

	fgets(buffer, 20 * sizeof(char), stdin);
	buffer[strcspn(buffer, "\n")] = 0;

	rc = send(socket, buffer, strlen(buffer)+1, 0);
	if (rc < 0)
		err("send");

	time = clock();
	rc = recv(socket, file_buffer, FILEBUFF, 0);
	time = clock() - time;

	if (rc < 0)
		err("recv");

	/*
	 * Drawback of doing this is, if my file starts with "ERROR"
	 * it won't consider the file to be valid
	 */
	if (!strcspn(file_buffer, "ERROR")) {
		printf("%s\n", file_buffer);
		return;
	}

	if (!flag) {
		printf("FILE CONTENTS:\n\n%s\n\n", file_buffer);
	} else {

		FILE *fptr;
		fptr = fopen(buffer, "wb");
		if (fptr == 0)
			err("fopen");
		
		fwrite(file_buffer, 
			sizeof(file_buffer) * sizeof(char), 1, fptr);
		printf("Created file %s!\n", buffer);
		fclose(fptr);
	}

	display_speed(time, strlen(file_buffer)+1);

	return;
}
