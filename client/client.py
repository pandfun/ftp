import socket
import json

FORMAT = "utf-8"

PORT = 9001
SERVER = "127.0.1.1"

ADDR = (SERVER, PORT)


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)
    print(f"[Connected to the server : {SERVER}:{PORT}]")

except Exception as e:
    print(f"Unable to connect to the server : {e}")
    exit()


# Function to send data to the server (via connection)
# Returns : { 0 : "Success", -1: "Fail" }
def sendData(data, connection: socket.socket):

    try:
        # Convert our data dictionary to a JSON-fromatted string
        jsonData = json.dumps(data)

        jsonDataLen = len(jsonData).to_bytes(4, byteorder="big")

        connection.sendall(jsonDataLen)
        connection.sendall(jsonData.encode(FORMAT))

        return 0

    except Exception as e:
        print(f"[Unable to send data to server\n{e}]")
        return -1


# Function to get data from the client (via connection)
# Returns : { data : "Success", None : "Fail" }
def recvData(connection: socket.socket):

    try:
        msgLenBytes = connection.recv(4)
        msgLen = int.from_bytes(msgLenBytes, byteorder="big")

        dataBytes = connection.recv(msgLen)
        data = json.loads(dataBytes.decode(FORMAT))

        return data

    except Exception as e:
        print(f"[Unable to recv data from server\n{e}]")
        return None


# Server Communication
def run():

    print("Type 'help' to see list of available commands")

    while True:
        command = input("~ (FTP) $ ")

        request = {}
        response = {}

        parsedCommand = command.split()

        commandName = parsedCommand[0]

        if commandName == "help":
            helpCmd()
            continue

        elif commandName == "exit":
            request["command"] = "exit"

        elif commandName == "list":
            if len(parsedCommand) > 2:
                printWrongUsage("list")
                continue

            request["command"] = "list"

            if len(parsedCommand) == 1:
                request["path"] = "."
            else:
                request["path"] = parsedCommand[1]

        elif commandName == "get":
            if len(parsedCommand) > 2:
                printWrongUsage("get")
                continue

            request["command"] = "get"
            request["fileName"] = parsedCommand[1]

        elif commandName == "put":
            if len(parsedCommand) > 2:
                printWrongUsage("put")
                continue

            request["command"] = "put"

            fileName = parsedCommand[1]
            fileContent = getFileContent(fileName)
            if fileContent is None:
                continue

            request["fileName"] = fileName
            request["fileContent"] = fileContent

        else:
            print(f"Command not found! Type 'help' to see list of all commands")
            continue

        sendStatus = sendData(request, server)
        if sendStatus < 0:
            break

        response = recvData(server)
        if response is None:
            break

        if response["status"] == "Fail":
            print(f"Server sent fail status : {response['response']}")
            continue

        if commandName == "get":
            createFile(request["fileName"], response["response"])
            continue

        print(f"{response['response']}")

        if commandName == "exit":
            break

    server.close()


def printWrongUsage(cmd):
    print("Wrong usage :", end=" ")

    if cmd == "list":
        print("list <path>")
    elif cmd == "get":
        print("get <file_name>")
    elif cmd == "put":
        print("put <file_name>")


def helpCmd():
    print(
        """usage : <cmd-name> <args>

    list - List all the files in the directory <dir-path>. 
    If there is no second argument, then it lists the server's root directory
    usage : list <dir-path>
    	
    	
    get - Get the file named <file-name> that is stored on the server
    usage : get <file-name>
    
    put - Store the file named <file-name> on the server
    usage : put <file-name>
    """
    )


# Function to create file
# Returns : { None }
def createFile(fileName, fileContent):

    try:
        with open(fileName, "w") as file:
            file.write(fileContent)

            print("[File Created!]")

    except Exception as e:
        print(f"[Failed to create file, try again\n{e}]")


# Function to send the file contents
# Returns : { FileContent : "Success", None : "Fail"}
def getFileContent(fileName):

    try:
        with open(fileName, "r") as file:
            file_content = file.read()

            return file_content

    except FileNotFoundError:
        print(f"Error: {fileName} not found!")

    except Exception as e:
        print(f"Error\n{e}")

    return None


run()
