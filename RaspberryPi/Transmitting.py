# Import Python libraries
import socket

# Import custom functions
from Flag import FLAG

def Transmit(flags: FLAG):    
    # Inputs:
    #   flags - FLAG class object
    pass

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    ####################
    ### From ChatGPT ###
    ####################

    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    # send a message
    message = b'This is beans!'
    print('sending "%s"' % message)
    sock.sendall(message)

    # receive the response and print it
    data = sock.recv(1024)
    print('received "%s"' % data)

    # clean up the socket
    sock.close()

    ####################
    ### From ChatGPT ###
    ####################