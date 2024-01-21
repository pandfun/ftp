import os


def listDir(dir="."):
    res = ""

    try:
        files = os.listdir(dir)
        for file in files:
            res += file + " "

    except FileNotFoundError:
        res = f"Dir '{dir}' not found"
    except PermissionError:
        res = f"Missing permissions to access '{dir}'"

    return res
