import socket
import json

FORMAT = "utf-8"

PORT = 9004
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)


# Connect to the server
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[Connected to the server : {SERVER}]")

except Exception as e:
    print(f"Unable to connect to the server : {e}")
    exit()


# Function to send data to the server (via connection)
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
        print(f"[Unable to send data to server : {e}]")
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
        print(f"[Unable to recv data from server : {e}]")
        return None


# Server Communication
def run():

    while True:
        msg_content = input("You: ")

        msg = {}
        msg["content"] = msg_content

        # Send message to server
        send_status = send_data(msg, client)
        if send_status < 0:
            break

        # Recv response from server
        reply = recv_data(client)
        if reply == None:
            break

        reply_status = reply["status"]
        reply_content = reply["content"]

        if reply_status == "Fail":
            print(f"[Server returned a fail status! - {reply_content}]")
            continue

        if msg_content == "get":
            print(f"    => Server : {reply_content}", end="")
            file_name = input(" : ")

            file_name_info = {"content": ""}
            file_name_info["content"] = file_name

            send_status = send_data(file_name_info, client)

            file_content = recv_data(client)
            if file_content == None:
                break

            if file_content["status"] == "Fail":
                print(f"Server : {file_content['content']}")
                continue

            print("[Adding File..]")
            create_file(file_name, file_content["content"])

            continue

        print(f"Server : {reply_content}")

        if msg_content == "exit":
            break

    print("[Terminating...]")
    client.close()


# Function to create file
# Returns : { None }
def create_file(file_name, file_content):

    try:
        with open(file_name, "w") as file:
            file.write(file_content)

            print("[File Created!]")

    except Exception as e:
        print(f"[Failed to create file, try again : {e}]")


run()