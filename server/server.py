import socket
import threading

from clientHandler import handleClient

PORT = 9002
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def run():
    server.listen()
    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()

        print(f"[Active Clients - {threading.active_count() - 1}]")


print(f"Listening for connections on {SERVER}")
run()
