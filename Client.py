import socket
import threading
import tkinter

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))

window = tkinter.Tk()
window.title("Connected To: "+ hostIp+ ":"+str(portNumber))

txtMessages = tkinter.Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

txtYourMessage = tkinter.Entry(window, width=50)
txtYourMessage.insert(0, "Type your message...")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def sendMessage():
    my_username = txtYourMessage.get()
    txtMessages.insert(tkinter.END, "\n" + "You: "+ my_username)
    clientSocket.send(my_username.encode("utf-8"))

btnSendMessage = tkinter.Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMessages.insert(tkinter.END, "\n" + serverMessage)

recvThread = threading.Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

window.mainloop()