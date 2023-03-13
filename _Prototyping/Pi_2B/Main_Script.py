### Main Raspberry Pi Loop ###

# Import python libraries
from pathlib import Path
import cv2
import os
import time

# Import created functions
# import Saving
# import Compression

# Create flags class
class FLAG:
    # Class initialization
    def __init__(self):
        # Set flags
        self.RECORD      = 0  # 1 if recording video
        self.TRANSMIT    = 0  # 1 if ready to transmit video files
        self.FOLDER      = 0  # 1 if files are present in the uncompressed image folder
        self.EQUAL       = 0  # 1 if same number of files in compressed and uncompressed image folders
        self.METHOD      = 0  # 0 for no compression
                              # 1 for JPEG2000
                              # 2 for Run-length encoding
                              # 3 for Dynamic Huffman encoding
                              # 4 for Static Huffman encoding
        self.ACTIVE      = 0  # 1 if compression algorithm is running
        self.COMPQUAL    = 60 # Compression quality (x % of original quality)

        # Create compressed/uncompressed directories
        self.p = Path(__file__).parent # Set path at current working directory (cwd)
        self.u = self.p / 'Uncompressed'
        self.c = self.p / 'Compressed'
        # self.RemoveDirectories() # Comment out if using Windows system
        self.CreateDirectories()
    
    def RemoveDirectories(self):
        # Remove image directories on launch
        os.system("rm -r " + str(self.c))
        os.system("rm -r " + str(self.u))
    
    def CreateDirectories(self):
        # Create image directories if they don't yet exist
        if not self.u.exists():
            self.u.mkdir(parents=True, exist_ok=False)
        if not self.c.exists():
            self.c.mkdir(parents=True, exist_ok=False)
    
    # Update all flag values
    def UpdateFlags(self):
        self.CheckFolder()
        self.CheckEqual()
        self.CheckTransmit()

    # Check if transmit flag should be updated
    def CheckTransmit(self):
        if not self.RECORD and self.FOLDER and self.EQUAL:
            self.TRANSMIT = 1

    # Check if folder flag should be updated
    def CheckFolder(self):
        self.FOLDER = any(list(self.u.glob('*.png')))

    # Check if anything exists in the compressed folder
    def CheckCompressedFolder(self):
        return any(list(self.c.glob('*.png')))

    # Check if equal flag should be updated
    def CheckEqual(self):
        self.EQUAL = len(list(self.u.glob('*.png'))) == len(list(self.c.glob('*.png')))

class Arm:
    # Class initialization
    def __init__(self):
        self.ACTION = 0 # 0 for fully closed
                        # 1 for fully opened
                        # 2 for stop in place
                        # 3 for loop
        self.STATUS = 0

    # Send action command to Arduino
    def SendAction(self):
        pass
    
if __name__ == "__main__":
    
    # Initialize flag class
    flags = FLAG()

    # Connect camera
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Cannot open camera. Exiting...")
        # exit()

    # Connect to arm
    print('Done')
    print()
    # # Begin main loop
    # while True:
    #     # Update flags
    #     flags.UpdateFlags(u, c)

    #     # Display GUI

    #     # Run frame saving (if needed)
    #     if flags.RECORD:
    #         pass

    #     # Run compression algorithm (if needed)
    #     if flags.FOLDER:
    #         pass

    #     # Run transmit algorithm (if needed)
    #     if flags.TRANSMIT:
    #         pass