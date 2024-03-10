# Multithreaded FTP Server-Client Model


## Table of Contents
- [How to use?](#how-to-use)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Documentation](#documentation)


---


## How to use
- ### Running the Server
  The directory in which the `server` folder is placed, will be treated as the "server"

  To start the server, run : 
  ```bash
  python server/server.py
  ```
  
> [!NOTE]  
> Execute this command from the "server" directory

<br>

- ### Running the Client
  You can keep the `client.py` file anywhere except for the same directory as the "server".

  To connect to the server, run : 
  ```bash
  python client.py
  ```

  <br><br>

> [!IMPORTANT]  
> Both the `server.py` and `client.py` files have macros for the Server's IP and Port.
> 
> By default, the IP Address (*the `SERVER` Macro*) is set to the local host, so client and server have to be on the same machine.
> 
> If you want to run the server and client from different machines, then replace the macro with the IP Address of the ***machine on which the server is running***

---


## Documentation

*Work-in-progress*

