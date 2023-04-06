# Import Python libraries
import serial
from time import sleep

class Arm:
    # Class initialization
    def __init__(self):
        # Create and open serial communiccation object
        # self.COM = serial.Serial('/dev/tty/AMA0', baudrate=9600) # Pin connection
        self.COM = serial.Serial('/dev/serial0', baudrate = 9600) # USB connection

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    com = Arm()
    # Reopen communication port
    if com.COM.is_open:
        com.COM.close()
    com.COM.open()

    iter = 1000

    # Write outputs for Arduino testing
    for _ in range(iter):
        com.COM.write(b'0')
        print('0')
        
    for _ in range(iter):
        com.COM.write(b'1')
        print('1')
        
    for _ in range(iter):
        com.COM.write(b'2')
        print('2')