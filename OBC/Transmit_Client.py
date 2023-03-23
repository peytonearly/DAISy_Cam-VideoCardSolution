# Import Python libraries
import socket

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    ####################
    ### From ChatGPT ###
    ####################

    ipAddress = "127.0.1.1"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ipAddress, 5555))

    data = s.recv(1024)
    print(data.decode("utf-8"))

    while True:
        message = input("Enter a message to send to the server: ")
        s.send(bytes(message, "utf-8"))
        data = s.recv(1024)
        print(data.decode("utf-8"))
    
    s.close()
        
    ####################
    ### From ChatGPT ###
    ####################