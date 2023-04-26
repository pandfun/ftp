/* Including standard headers */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <unistd.h>
#include <dirent.h>
#include <errno.h>


/* Macros */

#define FILEBUFF 10000
#define BUFFSIZE 1000


/* Function prototypes */

void err(char *);