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