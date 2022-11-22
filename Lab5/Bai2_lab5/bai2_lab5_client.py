from socket import *

sock = socket(AF_INET, SOCK_STREAM)

serverAddress = ('localhost',8888)
sock.connect(serverAddress)

try:
    print('Input a integer number from 0 to 9: ')
    number = input()
    print('Send: ',number)
    sock.sendall(number.encode())

    amount_received = 0
    amount_expected = len(number)
    msg = []

    while amount_received < amount_expected:
        data = sock.recv(100)
        amount_received += len(data)
        msg.append(data)

    print('Receive: ' , b''.join(msg).decode())        
finally:
    print('Close socket!!')
    sock.close()