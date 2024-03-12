import os


# Command Name : 'list'
# Function to list server's contents
# Returns : { ListOfFiles : "Success", Error : "Fail" }
def list_dir(dir="."):

    response = {"status": "", "content": ""}

    try:
        files = os.listdir(dir)
        buffer = []

        # Add file type for each file
        for file in files:
            file_path = os.path.join(dir, file)
            file_type = "DIR " if os.path.isdir(file_path) else "FILE"
            buffer.append(f"{file_type} - {file}")

        # Add file info (type and name) to the response
        response["content"] = "\n"
        response["content"] += "\n".join(buffer)

        response["status"] = "Success"

    except FileNotFoundError:
        response["status"] = "Fail"
        response["content"] = f"Error: Directory [{dir}] not found!"

    except PermissionError:
        response["status"] = "Fail"
        response["content"] = f"Error: Permission denied to access [{dir}]!"

    except Exception as e:
        response["status"] = "Fail"
        response["content"] = f"Error : {e}"

    return response


# Command Name : 'copy'
# Function to send the file contents
# Returns : { FileContent : "Success", Error : "Fail"}
def get_file_content(file_name):

    response = {"status": "", "content": ""}

    try:
        with open(file_name, "r") as file:
            file_content = file.read()

            response["content"] = file_content
            response["status"] = "Success"

    except FileNotFoundError:
        response["status"] = "Fail"
        response["content"] = f"Error: {file_name} not found!"

    except Exception as e:
        response["status"] = "Fail"
        response["content"] = f"Error : {e}"

    return response


# Function to create a file on server
# Returns : { SuccessMsg : "Success", ErrorMsg : "Fail" }
def create_file(file_info):
    try:
        file_name = file_info["name"]
        file_content = file_info["content"]

        with open(file_name, "w") as file:
            file.write(file_content)

            return f"File {file_name} received and stored on server!"

    except Exception as e:
        return f"Error : {e}"
