# Import Python libraries
import socket

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    ####################
    ### From ChatGPT ###
    ####################

    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a specific address and port
    server_address = ('localhost', 10000)
    sock.bind(server_address)

    # listen for incoming connections
    sock.listen(1)

    while True:
        # wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from', client_address)

        # receive data and echo it back
        data = connection.recv(1024).upper()
        print('received "%s"' % data)
        connection.sendall(data)

        # clean up the connection
        connection.close()
        
    ####################
    ### From ChatGPT ###
    ####################