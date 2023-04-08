### Transmit File ###
## Acting as client ##

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

    # hostname = socket.gethostname()
    hostname = "192.168.137.122"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((hostname, 5555))
    s.listen(1)

    print(f"Server started. Waiting for client to connect...")

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    clientsocket.send(bytes("Welcome to the server!", "utf-8"))

    while True:
        data = clientsocket.recv(1024)
        if not data:
            break
        print(f"Received data from client: {data.decode('utf-8')}")
        clientsocket.send(bytes("I received your message!", "utf-8"))
    
    clientsocket.close()

    ####################
    ### From ChatGPT ###
    ####################