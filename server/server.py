import socket
import threading
import json

# Import all the command handlers
from commandHandler import *

FORMAT = "utf-8"

PORT = 9001

# Sets the server IP to local host
SERVER = socket.gethostbyname(socket.gethostname())
SERVER_ADDR = (SERVER, PORT)


MAX_CONNECTIONS = 10


# Function to create a server socket and bind it to the address
def createServer():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(SERVER_ADDR)

        return server
    except Exception as e:
        print(f"Failed to create server socket : {e}")

    return None


def startServer():
    server = createServer()
    if server is None:
        exit(1)

    # Start listening for incoming client connections
    server.listen(MAX_CONNECTIONS)

    print(f"Port = {PORT} & Server IP = {SERVER}")
    print(f"Listening for client connections..")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()

        # We do -1, so we don't count the thread on which the
        # server is listening for connections
        print(f"[Active Clients => {threading.active_count() - 1}]")


# Function to handle a client connection
def clientHandler(connection: socket.socket, addr):

    print(f"New connection : {addr}")

    while True:
        request = recvData(connection)
        if request is None:
            break

        response = {}

        command = request["command"]

        if command == "exit":
            response["status"] = "Success"
            response["response"] = "Closing the connection.."

        elif command == "list":
            response = listCmdHandler(request)

        elif command == "get":
            response = getCmdHandler(request)

        elif command == "put":
            response = putCmdHandler(request)

        sendStatus = sendData(response, connection)
        if sendStatus < 0:
            break

        if command == "exit":
            break

    connection.close()
    return


# Function to send data to the client
def sendData(data, connection: socket.socket):
    try:
        jsonData = json.dumps(data)
        jsonDataLen = len(jsonData).to_bytes(4, byteorder="big")

        connection.sendall(jsonDataLen)
        connection.sendall(jsonData.encode(FORMAT))

        return 0
    except Exception as e:
        print(f"Unable to send data to client\n{e}")
        return -1


# Function to receive data from the client
def recvData(connection: socket.socket):
    try:
        dataLenBytes = connection.recv(4)
        dataLen = int.from_bytes(dataLenBytes, byteorder="big")

        dataBytes = connection.recv(dataLen)
        data = json.loads(dataBytes.decode(FORMAT))

        return data
    except Exception as e:
        print(f"Unable to recv data from the client\n{e}")
        return None


# Running the server
startServer()
