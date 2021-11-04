# Name: Angelina Boudro
# Program: Server.py This program will implement a server connection that will
# process requests from the client connection for the requested files.
# Date: Created - 07/23/2020, Last Modified - 11/03/2021

import socket
from threading import Thread

TCP_IP = '10.0.0.1' # this is the specified IP found in Mininet
TCP_PORT = 9001 # port number
BUFFER_SIZE = 1024

# Worker class for incoming client connections and requests
class ClientThread(Thread):

# The following will define self ip, port#, socket
    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port # port number
        self.sock = sock # socket number
        print(' New thread started for ' + ip + ":" + str(port)) # A new thread created for incming client

    def run(self):
        filename = input('File name: ') # Requested file name to ensure it is on the list
        f = open(filename, 'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Awaiting for incoming connections...")
    # The following will connect to the specified ip and port
    (conn, (ip, port)) = tcpsock.accept()
    # String line
    print('Incoming connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()

    break
socket.close()
tcpsock.close()

#end of server.py
