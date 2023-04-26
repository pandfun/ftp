all :
	make client
	make server
	rm -f *.o


# Client
client : client.o connect_client.o client_interactions.o err.o
	gcc client.o connect_client.o client_interactions.o err.o -o r_client

# Client files

client.o : client/client.c 
	gcc -c client/client.c

connect_client.o : client/connect_client.c
	gcc -c client/connect_client.c

client_interactions.o : client/client_interactions.c
	gcc -c client/client_interactions.c


# Server
server : server.o connect_server.o server_interactions.o err.o file_interactions.o
	gcc server.o connect_server.o server_interactions.o err.o file_interactions.o -o r_server

# Server files

server.o : server/server.c
	gcc -c server/server.c

connect_server.o : server/connect_server.c
	gcc -c server/connect_server.c

server_interactions.o : server/server_interactions.c
	gcc -c server/server_interactions.c

file_interactions.o : server/file_interactions.c
	gcc -c server/file_interactions.c


# Core files
err.o : core/err.c
	gcc -c core/err.c


# Clean
clean :
	rm -f *.o r_client r_server
