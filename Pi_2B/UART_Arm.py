import serial
from time import sleep

# Create and open serial communication object
com = serial.Serial('/dev/ttyAMA0', baudrate=9600)

# Reopen communication port
if com.is_open:
    com.close()
com.open()

# Write outputs for Arduino testing
for _ in range(100):
    com.write('0'.encode('utf-8'))
    print('0')
    sleep(0.5)
    
    com.write('1'.encode('utf-8'))
    print('1')
    sleep(0.5)
    
    com.write('2'.encode('utf-8'))
    print('2')
    sleep(0.5)
    
    com.write('3'.encode('utf-8'))
    print('3')
    sleep(0.5)