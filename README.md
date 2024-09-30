 Sweet-1
 # Real time chat Application in Python

This repository contains a simple chat application implemented in Python using sockets. The application consists of two main files: `server.py` and `client.py`. Follow the steps below to set up and run the chat application.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [How it Works](#how-it-works)
4. [Contributing](#contributing)


## 1. Installation

- Clone the repository to your local machine:

  ```bash
  git clone https://github.com/dhruv-joshi25/Real-time-chat-application
  ```

- Navigate to the project directory:

  ```bash
  cd chat-application-python
  ```

## 2. Usage

### Running the Server

1. Open a terminal and navigate to the project directory.

2. Start the server by running:

   ```bash
   python server.py
   ```

3. The server will start listening for incoming connections.

### Running the Client

1. Open another terminal window or multiple terminals for different clients.

2. Start a client by running:

   ```bash
   python client.py
   ```

3. You can now start chatting with other connected clients.

## 3. How it Works

- The `server.py` file sets up a socket server that listens for incoming connections.

- The `client.py` file connects to the server and allows users to send and receive messages.

- Communication between the server and clients is achieved through socket programming.

## 4. Contributing

Feel free to contribute to the development of this chat application. If you have any improvements or new features to suggest, please open an issue or create a pull request.


