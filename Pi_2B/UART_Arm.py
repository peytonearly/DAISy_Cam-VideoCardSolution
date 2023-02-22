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
    com.write('0'.encode('utf-8'))
    print('0')
    
for _ in range(iter):
    com.write('1'.encode('utf-8'))
    print('1')
    
for _ in range(iter):
    com.write('2'.encode('utf-8'))
    print('2')
    
    # com.write('3'.encode('utf-8'))
    # print('3')
    # sleep(0.5)