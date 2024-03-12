import socket
import threading
import json

from commands import *

FORMAT = "utf-8"

PORT = 9004
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def run():
    server.listen()
    print(f"Listening for connections on port {PORT}...")

    while True:

        conn, addr = server.accept()

        thread = threading.Thread(target=handleClientConn, args=(conn, addr))
        thread.start()

        print(f"[Active Client => {threading.active_count() - 1}]")


# Client handler function
def handleClientConn(conn: socket.socket, addr):

    print(f"New Connection : {addr}")

    while True:
        msg = recv_data(conn)
        if msg == None:
            break

        reply = {"status": "Success", "content": "Command Not Found"}

        msg_content = msg["content"]

        if msg_content == "exit":
            reply["content"] = "Closing connection.."

        elif msg_content == "hi":
            reply["content"] = "Hello client, this is server speaking"

        elif msg_content == "list":
            reply = list_dir()

        elif msg_content == "get":
            reply["content"] = "Enter the name of the file"

            send_status = send_data(reply, conn)
            if send_status < 0:
                break

            file_name_info = recv_data(conn)
            if file_name_info == None:
                break

            reply = get_file_content(file_name_info["content"])

        elif msg_content == "put":
            reply["content"] = "Enter name of the file to upload"
            send_status = send_data(reply, conn)
            if send_status < 0:
                break

            file_info = recv_data(conn)
            if file_info == None:
                break

            if file_info["status"] == "Fail":
                reply["content"] = "Aborting file upload"
            else:
                file_create_status = create_file(file_info)
                reply["content"] = file_create_status

        # Sending the response to client
        send_status = send_data(reply, conn)
        if send_status < 0:
            break

        if msg_content == "exit":
            break

    conn.close()


# Function to send data to the client (via connection)
# Returns : { 0 : "Success", -1: "Fail" }
def send_data(data, connection: socket.socket):

    try:
        # Convert our data dictionary to a JSON-fromatted string
        json_data = json.dumps(data)

        msg_len = len(json_data).to_bytes(4, byteorder="big")

        connection.sendall(msg_len)
        connection.sendall(json_data.encode(FORMAT))

        return 0

    except Exception as e:
        print(f"[Unable to send data to client : {e}]")
        return -1


# Function to get data from the client (via connection)
# Returns : { data : "Success", None : "Fail" }
def recv_data(connection: socket.socket):

    try:
        msg_len_bytes = connection.recv(4)
        msg_len = int.from_bytes(msg_len_bytes, byteorder="big")

        data_bytes = connection.recv(msg_len)
        data = json.loads(data_bytes.decode(FORMAT))

        return data

    except Exception as e:
        print(f"[Unable to recv data from client : {e}]")
        return None


run()
