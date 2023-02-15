### Main Raspberry Pi Loop ###

import cv2
import numpy as np
from PIL import Image
import os

# Create flags class
class FLAG:
    # Class initialization
    def __init__(self):
        self.RECORD      = 0 # 1 if recording video
        self.TRANSMIT    = 0 # 1 if ready to transmit video files
        self.FOLDER      = 0 # 1 if files are present in the uncompressed image folder
        self.EQUAL       = 0 # 1 if same number of files in compressed and uncompressed image folders
        self.COMPRESSION = 0 # 0 for no compression, else number TBD
    
    # Update all flag values
    def UpdateFlags(self):
        self.CheckTransmit()
        self.CheckFolder()
        self.CheckEqual()

    # Check if transmit flag should be updated
    def CheckTransmit(self):
        if not self.RECORD and self.FOLDER and self.EQUAL:
            self.TRANSMIT = 1

    # Check if folder flag should be updated
    def CheckFolder(self):
        pass

    # Check if equal flag should be updated
    def CheckEqual(self):
        pass

# Create compressed/uncompressed directories

# Connect camera

# Connect to arm

# Begin main loop
while True:
    # Update flags

    # Display GUI

    # Run frame saving (if needed)

    # Run compression algorithm (if needed)

    # Run transmit algorithm (if needed)