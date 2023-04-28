#include "../core/core.h"
#include "server.h"



/*
 * Function used for listing contents of pwd
 *
 * Flags Translation: 
 * 0 -> normal
 * 1 -> hidden files
 * 
 * If more flags are added, update them here!
 */
void list_dir(int socket, int flag)
{
	DIR *dr = opendir(".");
	if (dr == NULL)
		err("opendir");
	
	char transfer_buff[BUFFSIZE] = {0};

	struct dirent *dir;

	int space_left = BUFFSIZE;
	int cur_len = 0;

	while ((dir = readdir(dr)) != NULL) {

		if (flag == 0 && strchr(dir->d_name, '.') == dir->d_name)
			continue;
		
		// +2 to include the newline and null
		cur_len = strlen(dir->d_name) + 2;

		if (cur_len <= space_left) {

			strcat(transfer_buff, dir->d_name);
			strcat(transfer_buff, " ");

		} else {

			memset(transfer_buff, 0, 
				strlen(transfer_buff) * sizeof(char));
			strcat(transfer_buff, 
				"Error: could not include all file names!");

			break;

		}

		space_left -= cur_len;
	}


	closedir(dr);
	
	strcat(transfer_buff, "\n");
	send(socket, transfer_buff, strlen(transfer_buff)+1, 0);

	return;
}


/*
 * This function will look for a file in the pwd
 * and send it to the client in a file buffer
 */
void send_file(int socket)
{
	int rc;
	char file_name[20] = {0};
	char filebuff[FILEBUFF];
	FILE *fptr;

	rc = recv(socket, file_name, 20 * sizeof(char), 0);
	if (rc < 0)
		err("recv");
	
	/* 
	 * TODO : default fail case is to terminate program
	 * Fix so it alerts the client and gives them another 
	 * chance to enter the file name or cancel operation
	 * 
	 * Cur Behaviour : Detects file not found, server terminates
	 * but client will still be active, which will also 
	 * eventually terminate 
	 */
	fptr = fopen(file_name, "rb");
	if (fptr == 0)
		err("fopen");
	
	/* TODO : check for fail case */
	fread(filebuff, sizeof(filebuff), 1, fptr);

	rc = send(socket, filebuff, strlen(filebuff)+1, 0);
	if (rc < 0)
		err("send");
	
	fclose(fptr);

	return;
}