# CSC340 Project 1: File Transfer and Word Count

This project showcases a client-server application implemented in Java, designed to securely transfer a text file (`words.txt`) from a server to multiple clients. Additionally, the project includes a `WordCount` utility to analyze the transferred file and count the total number of words.

## 📂 Project Structure
- `Client/Client.java`: Client-side application that connects to the server, receives the file, and saves it locally as `received_words.txt`.
- `Client/Server.java`: Server-side application that handles incoming client connections, sends the `words.txt` file, and limits connections to five clients.
- `Client/WordCount.java`: A utility class that reads a text file and counts the number of words it contains.

## 🔑 Key Features
- **Multi-Client Support**: The server can handle up to 5 concurrent client connections using multithreading.
- **File Transfer**: Secure transmission of a text file over sockets.
- **Word Count Utility**: Analyzes the received file and outputs the total word count.
- **Error Handling**: Includes checks for file existence, connection errors, and graceful shutdown of sockets.
