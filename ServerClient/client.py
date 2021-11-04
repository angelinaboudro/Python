# Name: Angelina Boudro
# Program: Client.py this program will implement a client connection that will request a
# file from the list from the server.
# Date: Created - 07/23/2020, Last Modified - 11/3/2021

import sys
import os
from os import path
import socket

# this will retrieve the client object
f_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the following will connect to the server with inet_addr and port
f_client.connect(('10.0.0.1', 9001))

file_name_to_read = input("Enter Filename to download from server : ")
directoryname = input("Enter the directory : ")
fullPath = directoryname + os.sep + file_name_to_read
# will display the full path of where the file is located
print("fullpath = ", fullPath)
rec_data = "Temp"

while True:
    # this will read the file
    f_client.send(fullPath.encode())
    rec_data = f_client.recv(1024)

    curr_dir = os.getcwd()

    # the following will create a directory
    clientpath = curr_dir + os.sep + "ClientFolder"
    if (os.path.isdir(clientpath)):
        print("Client folder already exists.") # In the case that a specified folder already exists
    else:
        os.mkdir(clientpath)
    # this will open the file for writing
    fDownloadFile = open(clientpath + os.sep + file_name_to_read, "wb")
    while rec_data:
        fDownloadFile.write(rec_data)  # downloading the file
        rec_data = f_client.recv(1024)  # client received the file
    print("Success! File received from server.")
    break

f_client.close()

# end of client.py
