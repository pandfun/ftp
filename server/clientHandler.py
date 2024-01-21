import socket
from commands import ls


BUFF_SIZE = 64
FORMAT = "utf-8"
DISCON_MSG = "exit"


def handleClient(conn: socket.socket, addr):

    print(f"New Connection : {addr}")

    # Function to send messages to client
    def send(msg):
        message = msg.encode(FORMAT)

        msgLen = len(message)
        sendLen = str(msgLen).encode(FORMAT)

        # Padding the msg so it fills the full buff length
        sendLen += b" " * (BUFF_SIZE - len(sendLen))

        conn.send(sendLen)
        conn.send(message)

    # Function to receive messages from the client
    def recv():
        # Fixes the issue where we may not know the length of the incoming
        # client message. This is designed so that the first messages that the
        # client sends is the length of the incoming message.
        # The next recv will get the actual message
        msgLen = conn.recv(BUFF_SIZE).decode(FORMAT)
        if not msgLen:
            return

        msg = conn.recv(int(msgLen)).decode(FORMAT)

        return msg

    while True:
        msg = recv()
        reply = ""

        if msg == DISCON_MSG:
            reply = "CLosing connection"
        elif msg == "ls":
            reply = ls.listDir()

        send(reply)

        if msg == DISCON_MSG:
            break

    conn.close()
