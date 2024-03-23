# Multithreaded FTP Server-Client Model


## Table of Contents
- [Usage](#usage)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Features](#features)
  - [Implemented](#implemented)
  - [Pending](#pending)

---


## Usage

> [!IMPORTANT]  
> Both the `server.py` and `client.py` files have macros (*variables*) for the Server's IP and Port.
> 
> By default, the IP Address (*the `SERVER` Macro*) is set to the local host.
> So client tries to connect to it's local host (which may not work if the server is on a different machine).
> 
> If you want to run the server and client from different machines, replace the macro with the IP Address of the ***machine on which the server is running***


- ### Running the Server
  The directory in which the `server` folder is placed, will be treated as the "server"

  To start the server, run : 
  ```bash
  python server/server.py
  ```
  
> [!IMPORTANT]
> Execute this command from the "server" directory to ensure files are stored and fetched from the correct directory.

<br>

- ### Running the Client
  You can keep the `client.py` file anywhere except for the same directory as the "server".

  To connect to the server, run : 
  ```bash
  python client.py
  ```

---


## Features

- ### Implemented
  - [x] **Concurrent client connections** - Allow multiple clients to connect to the server simultaneously, improving scalability and responsiveness.
  - [x] **Upload _(put)_ files** - Allow clients to transfer files to the server.
  - [x] **Download _(get)_ files** - Allow clients to retrieve files from the server.

- ### Pending
  - [ ] **File locking** - Implement file locking mechanisms to prevent conflicts when multiple clients attempt to access or modify the same file simultaneously.
  - [ ] **File compression and descompression** - Introduce file compression techniques to optimize storage space on the server and minimize data transfer times.
  - [ ] **File encryption** - Enhance security by encrypting files during transmission to protect sensitive data from unauthorized access.
  - [ ] Directory navigation commands
  - [ ] **Transfer multimedia files** - Extend file transfer capabilities to support multimedia files, so users can share images, videos, and audio files.
  - [ ] **User authentication** - Implement user authentication to authenticate users and restrict access of secure servers.
  - [ ] **Improved server logging** - Better server logging to record detailed information about client activities and server events for auditing and troubleshooting purposes.

  
---

<br>
