# Multithreaded FTP Server-Client Model


## Table of Contents
- [How to use?](#how-to-use)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Features](#features) (wip)
- [Documentation](#documentation) (wip)


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
> Both the `server.py` and `client.py` files have macros (*variables*) for the Server's IP and Port.
> 
> By default, the IP Address (*the `SERVER` Macro*) is set to the local host.
> So client tries to connect to it's local host (which may not connect to the correct server if you're using them from different machines).
> 
> If you want to run the server and client from different machines, replace the macro with the IP Address of the ***machine on which the server is running***


---


## Features

*Work-in-progress*

---


## Documentation

*Work-in-progress*

