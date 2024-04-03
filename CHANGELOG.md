# Changelog

All notable changes to this project will be documented in this file.

## 3 Apr, 2024
- Implemented server-side file locks. This prevents multiple clients from accessing the same file and causing race conditions

## 2 Apr, 2024

- Client parses the command arguments directly, just like how it would be done in a terminal
- File names and contents are sent with `GET` and `PUT` commands, eliminating the need for additional socket data transfers
- Improved naming convention for JSON keys in both the `request` and `response`
- New `help` command to assist users with available functionality
- Improved error handling
<br><br>
- Updated command usage 
  - LIST - `list <dir-path>` (If there is no second argument, then it lists the server's root directory)
  - GET - `get <file-name>`
  - PUT - `put <file-name>`
