### Raspberry Pi Main File ###

# Import Built-In Python libraries
from pathlib import Path
import tkinter as tk
import subprocess
import os
import datetime

import multiprocessing as mp

# # Install required libraries
# print("Installing required libraries.")
# subprocess.call("Install_Reqs.sh", shell=True)
# print("Libraries installed.")

# Import libraries
import cv2
import serial

# Import project files
from Flag import FLAG
import GUI
from Arm_Control import Arm
from Compressing import Compression
from Saving import SaveFrame
from Transmiting import Transmit

#########################
### Project Functions ###
#########################

#########################
### Project Main Code ###
#########################
if __name__ == "__main__":
    # Initialize classes and variables
    flags = FLAG()
    flags.METHOD = 1
    flags.RECORD = 1
    flags.COMNAME = 'COM6' # Uncomment and update to current system if no RPi
    compProcess = mp.Process()
    transmitProcess = mp.Process()

    # Open camera
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Camera failed to open.")
        exit(1)

    # Open com port (reopen if already open)
    # com = serial.Serial(flags.COMNAME, baudrate=9600)
    # if com.is_open():
    #     com.close()
    # com.open()

    running = True

    # while running:
    for _ in range (1000):
        # Update flags
        flags.UpdateFlags()

        # Read frame
        ret, frame = cam.read()

        # Determine if frame should be saved
        if ret and flags.RECORD:
            SaveFrame(flags, frame)

        # Determine if compression should run
        if not flags.EQUAL:
            if compProcess.exitcode is None and not compProcess.is_alive(): 
                # Process hasn't exited and isn't running
                # Start a new process
                compProcess = mp.Process(target=Compression, args=[flags])
                compProcess.start()
                print("Compression process ", compProcess.pid, " started..")
            elif compProcess.is_alive():
                # Process hasn't exited but is running 
                # Do nothing
                # print("-- Process ", compProcess.pid, " still running. --")  # Debug statement
                pass
            elif not compProcess.is_alive() and compProcess.exitcode == 0: 
                # Process has exited without error
                compProcess.join()
                print("Compression process ", compProcess.pid, " finished successfully.")
                
                # Create a new process
                compProcess = mp.Process(target=Compression, args=[flags])
                compProcess.start()
                print("Compression process ", compProcess.pid, " started.")
            elif compProcess.exitcode > 0: 
                # Process exited with error
                print("== ERROR: Compression process ", compProcess.pid, " terminated with error ", compProcess.exitcode, " ==")
            else:
                # print("Shouldn't ever get here") # Debug statement 
                pass
                
        # Determine if files should be transmitted
        if flags.TRANSMIT:
            if transmitProcess.exitcode is None and not transmitProcess.is_alive(): 
                # Process hasn't exited and isn't running
                # Start a new process
                transmitProcess = mp.Process(target=Compression, args=[flags])
                transmitProcess.start()
                print("Transmit process ", transmitProcess.pid, " started..")
            elif transmitProcess.is_alive():
                # Process hasn't exited but is running 
                # Do nothing
                # print("-- Process ", transmitProcess.pid, " still running. --")  # Debug statement
                pass
            elif not transmitProcess.is_alive() and transmitProcess.exitcode == 0: 
                # Process has exited without error
                transmitProcess.join()
                print("Transmit process ", transmitProcess.pid, " finished successfully.")
                
                # Create a new process
                transmitProcess = mp.Process(target=Transmit, args=[flags])
                transmitProcess.start()
                print("Transmit process ", transmitProcess.pid, " started.")
            elif transmitProcess.exitcode > 0: 
                # Process exited with error
                print("== ERROR: Transmit process ", transmitProcess.pid, " terminated with error ", transmitProcess.exitcode, " ==")
            else:
                # print("Shouldn't ever get here") # Debug statement 
                pass

        # Send movement command to arm
            # com.write(flags.ARMCMD.to_bytes())
        
        # Receive serial output from arduino
            # comData = com.read_until()
            # Do something with comData

    # Program shutdown tasks
    # com.close()
