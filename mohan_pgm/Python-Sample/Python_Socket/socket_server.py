##from multiprocessing.connection import Listener
##
##address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
##listener = Listener(address, authkey='secret password')
##conn = listener.accept()
##print 'connection accepted from', listener.last_accepted
##while True:
##    msg = conn.recv()
##    # do something with msg
##    if msg == 'close':
##        conn.close()
##        break
##listener.close()


import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = raw_input()
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
