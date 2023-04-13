# Import Python libraries
import serial
import keyboard

com_port = 'COM6'

if __name__ == "__main__":
    # com = serial.Serial(com_port, baudrate=19200)
    com = serial.Serial(com_port, baudrate=9600)
    
    # Reopen serial port if open
    if com.is_open:
        com.close()
    com.open()

    # Initialize transmit variable
    signal = 0

    # Main loop
    while True:
        if keyboard.is_pressed("q"): # Stop program
            print("Stopping program.")
            exit()
        if keyboard.is_pressed("0"): # Stop arm
            signal = 0
        if keyboard.is_pressed("1"): # Open arm
            signal = 1
        if keyboard.is_pressed("2"): # Close arm
            signal = 2
        if keyboard.is_pressed("3"): # Loop open/closed
            signal = 3
        
        # Send signal to arduino
        # com.write(signal.to_bytes())
        com.write(signal)
        print(signal)