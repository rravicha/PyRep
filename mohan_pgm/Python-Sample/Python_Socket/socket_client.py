##from multiprocessing.connection import Client
##
##address = ('localhost', 6000)
##conn = Client(address, authkey='secret password')
##conn.send('close')
### can also send arbitrary objects:
### conn.send(['a', 2.5, None, int, sum])
##conn.close()


import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("wwwwwwwwwwwwwwwwww")
    message = raw_input("enter your message:")  # take input
    print(message)
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = raw_input()  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
