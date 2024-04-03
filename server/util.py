import os
from filelock import FileLock


def listDir(path):
    if path is None:
        path = "."

    response = {}

    try:
        files = os.listdir(path)
        buffer = []

        for file in files:
            filePath = os.path.join(path, file)
            fileType = "DIR" if os.path.isdir(filePath) else "FILE"
            buffer.append(f"{fileType} : {file}")

        response["response"] = "\n".join(buffer)

        response["status"] = "Success"

    except Exception as e:
        response["status"] = "Fail"
        response["response"] = f"Error\n{e}"

    return response


def getFileContent(fileName):

    response = {}

    fileLockName = fileName + ".lock"
    lock = FileLock(fileLockName)

    lock.acquire()
    try:
        with open(fileName, "r") as file:
            fileContent = file.read()

            response["response"] = fileContent
            response["status"] = "Success"

    except Exception as e:
        response["status"] = "Fail"
        response["response"] = f"Error\n{e}"

    finally:
        lock.release()
        if os.path.exists(fileLockName):
            os.remove(fileLockName)

    return response


def createFile(fileName, fileContent):

    response = {}

    fileLockName = fileName + ".lock"
    lock = FileLock(fileLockName)

    lock.acquire()
    try:
        with open(fileName, "w") as file:
            file.write(fileContent)

            response["status"] = "Success"
            response["response"] = f"File {fileName} received and stored on server!"

    except Exception as e:
        response["status"] = "Fail"
        response["response"] = f"Error\n{e}"

    finally:
        lock.release()
        if os.path.exists(fileLockName):
            os.remove(fileLockName)

    return response
