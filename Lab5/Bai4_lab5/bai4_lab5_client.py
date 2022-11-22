from socket import *
import os

# Create TCP/IP socket
socket_1 = socket(AF_INET, SOCK_STREAM)
socket_2 = socket(AF_INET, SOCK_STREAM)
# Connect the socket to the server listening port
serverAddress = ('localhost', 8000)
serverAddress2 = ('localhost', 8001)

socket_1.connect(serverAddress)

requestFromClient = input('Enter your request: ')

fileName = requestFromClient.split(' ')[1]
protocol = requestFromClient.split(' ')[0]
existsfolder = os.path.isdir(fileName)

socket_1.send(requestFromClient.encode())
# Response of the request
data = socket_1.recv(1024)
print('Response from server for the request => ', data.decode())

if data.decode() == 'OK':
    socket_2.connect(serverAddress2)
    if protocol == "GET":
        data1 = socket_2.recv(1024)
        f = open('newfile.txt', 'wb')
        f.write(data1)
        f.close()
        print('Copy file content from "' + fileName + '" into "newfile.txt" => successful')
        socket_2.close()
    if protocol == 'DELETE':
        data1 = socket_2.recv(1024)
        print(data1.decode())
else:
    socket_1.close()
    socket_2.close()