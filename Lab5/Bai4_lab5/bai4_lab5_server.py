from socket import *
from multiprocessing import connection
import os

socket_1 = socket(AF_INET, SOCK_STREAM)
socket_2 = socket(AF_INET, SOCK_STREAM)

serverAddress_1 = ('localhost', 8000)
serverAddress_2 = ('localhost', 8001)

socket_1.bind(serverAddress_1)
socket_2.bind(serverAddress_2)

socket_1.listen(5)
socket_2.listen(5)

while True:
    print('Start up on port 8000...')
    connection_1, clientAddress_1 = socket_1.accept()
    requestFromClient = connection_1.recv(1024)
    print('Request from client: ', requestFromClient.decode())
    data = (requestFromClient.decode()).split(' ')
    protocol = data[0]
    fileName = data[1]

    msgSuccessful = 'OK'
    msgError = 'ERROR'
    msgErrorRequest = 'Incorrect request'
    existsfile = os.path.exists(fileName)
    if existsfile == True:
        connection_1.send(msgSuccessful.encode())
        connection_2, clientAddress_2 = socket_2.accept()
        print('Start up on port 8001...')
        if protocol == 'GET':
            f = open(fileName, 'rb')
            while True:
                data_1 = f.read(1024)
                while (data_1):
                    connection_2.send(data_1)
                    data_1 = f.read(1024)
                if not data_1:
                    f.close()
                    print('Closing connection...')
                    connection_2.close()
                    break
            connection_2.close()
            break
        elif protocol == 'DELETE':
            print('Request from client: ', requestFromClient.decode())
            os.remove(fileName)
            msg = 'Delete ' + fileName + ' => successful'
            connection_2.send(msg.encode())
            break
        else:
            connection_2.send(msgErrorRequest.encode())
    else:
        connection_1.send(msgError.encode())
        print('Closing connection...')
        connection_1.close()
        break