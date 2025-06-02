# CSC340 Project 2: Trivia Game Client-Server System

This project implements a basic networked trivia game using Java, focusing on client-server communication over TCP and UDP. The server manages trivia questions, scores, and client connections, while the client interacts with the server through a simple GUI.

## 📂 Project Structure
- `Server.java`: Manages trivia questions, client connections, scoring, and communication.
- `ClientWindow.java`: Provides a GUI for players to view questions, select answers, and submit responses.
- `ClientHandler.java`: Handles individual client connections and score tracking.
- `TriviaQuestion.java`: Defines trivia questions, options, and correct answers.
- `QA.txt`: Contains the trivia questions and answers used during the game.

## 🔑 Key Features
- **Client-Server Architecture**: Server handles multiple clients concurrently using TCP sockets.
- **UDP Polling and Buzzers**: Clients use UDP to quickly notify the server of readiness to answer questions.
- **Trivia Game Logic**: Server selects questions from a pool, broadcasts them to clients, and processes submitted answers.
- **Scoring System**: Points awarded for correct answers and deducted for incorrect ones.
- **GUI-Based Client**: Simple interface for displaying questions and selecting answers.
