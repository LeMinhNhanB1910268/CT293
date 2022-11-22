from base64 import decode
from socket import *

print('Enter into a synthetic math: num1 math(+ - * /) num2 , Separated by space. vd: 1 + 2')
strs = input()
print('The expression you entered: ', strs)

strs = str.encode(strs)

serverAddressPort = ('localhost', 8888)
BufferSize = 8192

UDPClientSocket = socket(family= AF_INET, type= SOCK_DGRAM)

UDPClientSocket.sendto(strs, serverAddressPort)

messFromServer = UDPClientSocket.recvfrom(BufferSize)
mess = 'Result {}'.format(messFromServer[0].decode())
print(mess)



