'''
Created by Angelina Derkacheva
For Computer Networks
Project: Server using HTTP and socket.
'''

from socket import *
from socket import socket


def webserver():
    serverSocket: socket = socket(AF_INET, SOCK_STREAM)
    serverHost = 'localhost'
    recvBuffer = 1024
    serverPort: int = 80
    serverSocket.bind(('', 80))

    serverSocket.listen(1)
    print("Port: ", serverPort)

    while True:
        print("...ready to listen ")

        connectionSocket: socket
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)
            print(message)
            filename = message.split()[1]
            print(filename[1])
            print(filename, "", filename[1])

            f = open(filename[1:])
            outputdata = f.read()

            print(outputdata)

            connectionSocket.send("HTTP/ \r\n\r\n")


            connectionSocket.close()
        except IOError:
            print("404 Not Found")
            connectionSocket.send("""HTTP: 404 File Not Found \r\n""".encode());
        finally:
            pass
        break
    pass

if __name__ == "__main__":
    webserver()
