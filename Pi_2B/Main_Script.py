### Main Raspberry Pi Loop ###

from pathlib import Path
import cv2
import time

# Create flags class
class FLAG:
    # Class initialization
    def __init__(self):
        self.RECORD      = 0 # 1 if recording video
        self.TRANSMIT    = 0 # 1 if ready to transmit video files
        self.FOLDER      = 0 # 1 if files are present in the uncompressed image folder
        self.EQUAL       = 0 # 1 if same number of files in compressed and uncompressed image folders
        self.METHOD      = 0 # 0 for no compression
                             # 1 for JPEG2000
                             # 2 for H.264
                             # 3 for H.265
        self.ACTIVE      = 0 # 1 if compression algorithm is running
    
    # Update all flag values
    def UpdateFlags(self, u: Path(), c: Path()):
        self.CheckFolder(u)
        self.CheckEqual(u, c)
        self.CheckTransmit()

    # Check if transmit flag should be updated
    def CheckTransmit(self):
        if not self.RECORD and self.FOLDER and self.EQUAL:
            self.TRANSMIT = 1

    # Check if folder flag should be updated
    def CheckFolder(self, u: Path()):
        self.FOLDER = any(u.glob('*/*.png'))

    # Check if equal flag should be updated
    def CheckEqual(self, u: Path(), c: Path()):
        self.EQUAL = len(list(u.glob('*/*.png'))) == len(list(c.glob('*/*.png')))

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

    ### Create compressed/uncompressed directories ###
    p = Path(__file__).parent # Set path at current working directory (cwd)
    u = p / 'Uncompressed'
    c = p / 'Compressed'

    # Create image directories if they don't yet exist
    if not u.exists():
        u.mkdir(parents=True, exist_ok=False)
    if not c.exists():
        c.mkdir(parents=True, exist_ok=False)

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