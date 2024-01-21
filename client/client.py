import socket


BUFF_SIZE = 64
FORMAT = "utf-8"
DISCON_MSG = "exit"

PORT = 9002
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

validCommands = {"LS", "EXIT"}


try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"Connected to server {SERVER}")
except Exception as e:
    print(f"Unable to connect : {e}")
    exit()


def send(msg):
    message = msg.encode(FORMAT)

    msgLen = len(message)
    sendLen = str(msgLen).encode(FORMAT)

    # Padding the msg so it fills the full buff length
    sendLen += b" " * (BUFF_SIZE - len(sendLen))

    client.send(sendLen)
    client.send(message)


def recv():
    # Fixes the issue where we may not know the length of the incoming
    # client message. This is designed so that the first messages that the
    # client sends is the length of the incoming message.
    # The next recv will get the actual message
    msgLen = client.recv(BUFF_SIZE).decode(FORMAT)
    if not msgLen:
        return

    msg = client.recv(int(msgLen)).decode(FORMAT)

    return msg


def serverHandler():

    print(f"Connected to {SERVER}")
    print("Type 'help' to see list of available commands or 'exit' to quit")

    while (True):
        msg = input(">> ")

        if msg.upper() not in validCommands:
            print("Command not found!")
            continue

        send(msg)
        reply = recv()

        print(reply)

        if msg == "exit":
            break

    client.close()


serverHandler()
