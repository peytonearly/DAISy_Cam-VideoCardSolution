import serial
from time import sleep

# Create and open serial communication object
com = serial.Serial('/dev/ttyAMA0', baudrate=9600)
# com = serial.Serial('/dev/serial0', 9600)

# Reopen communication port
if com.is_open:
    com.close()
com.open()

iter = 1000

# Write outputs for Arduino testing
for _ in range(iter):
    com.write(b'0')
    print('0')
    
for _ in range(iter):
    com.write(b'1')
    print('1')
    
for _ in range(iter):
    com.write(b'2')
    print('2')
