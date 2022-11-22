from base64 import decode
from socket import *

localIP = 'localhost'
localPort = 8888
bufferSize = 8192

def calculate(str, num1, num2):
    if str == '+':
        kq = num1 + num2
    elif str == '-':
        kq = num1 - num2
    elif str == '/':
        kq = num1 / num2
    elif str == '*':
        kq = num1 * num2    
    else:
        kq = 'Invalid math'
    return kq

UDPServerSocket = socket(family=AF_INET, type=SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))
print('UDP Server')

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    strs = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientString = 'String sent from Client: {}'.format(strs.decode())

    arr = strs.decode().split()
    operant1 = int(arr[0])
    op = arr[1]
    operant2 = int(arr[2])

    result = str(calculate(op, operant1, operant2))
    print('Result: ' + result)
    sendresult = str.encode(result)

    UDPServerSocket.sendto(sendresult,address)