from socket import *
sock = socket(AF_INET, SOCK_STREAM)

serverAddress = ('localhost',8888)

print('Start add' , serverAddress)
sock.bind(serverAddress)
sock.listen(1)

def number_to_string(number):
    switcher = {
        0: 'Khong',
        1: 'Mot',
        2: 'Hai',
        3: 'Ba',
        4: 'Bon',
        5: 'Nam',
        6: 'Sau',
        7: 'Bay',
        8: 'Tam',
        9: 'Chin',
    }
    return switcher.get(number,'Not integer!!!!')

while True:
    print('Waiting for a connection')
    connection, clientAddress = sock.accept()
    try:
        print('Connection form', clientAddress)
        while True:
            data = connection.recv(50)
            print('Received: ' ,data.decode())

            if data:
                print('sending data back to the client address')
                data = int(data)
                result = number_to_string(data)
                connection.sendall(result.encode(), )
                break
            
            else:
                print('no data from', clientAddress)
                break
    finally:
        print('Closed connection!!')
        connection.close()