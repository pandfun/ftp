#include "core.h"

void err(char *msg)
{
        perror(msg);
        exit(1);
}