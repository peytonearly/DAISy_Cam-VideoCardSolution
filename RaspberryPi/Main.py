### Raspberry Pi Main File ###

# Import Built-In Python libraries
from pathlib import Path
import tkinter as tk
import subprocess
import os
import datetime

import multiprocessing as mp
import concurrent.futures

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
from Transmit_Server import Transmit

#########################
### Project Functions ###
#########################
def CompProcess():
    pass

#########################
### Project Main Code ###
#########################
if __name__ == "__main__":
    # Initialize classes and variables
    flags = FLAG()
    flags.METHOD = 0
    flags.RECORD = 1
    compProcess = mp.Process()

    # Open camera
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Camera failed to open.")
        exit(1)

    running = True

    while running:
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
                print("Process ", compProcess.pid, " started..")
            elif compProcess.is_alive():
                # Process hasn't exited but is running 
                # Do nothing
                # print("-- Process ", compProcess.pid, " still running. --")  # Debug statement
                pass
            elif not compProcess.is_alive() and compProcess.exitcode == 0: 
                # Process has exited without error
                compProcess.join()
                print("Process ", compProcess.pid, " finished successfully.")
                
                # Create a new process
                compProcess = mp.Process(target=Compression, args=[flags])
                compProcess.start()
                print("Process ", compProcess.pid, " started.")
            elif compProcess.exitcode > 0: 
                # Process exited with error
                print("== ERROR: Process ", compProcess.pid, " terminated with error ", compProcess.exitcode, " ==")
            else:
                print("Shouldn't ever get here")