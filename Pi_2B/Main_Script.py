### Main Raspberry Pi Loop ###

from pathlib import Path
import cv2

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
    def CheckFolder(self, u):
        self.FOLDER = any(u.iterdir())

    # Check if equal flag should be updated
    def CheckEqual(self, u, c):
        self.EQUAL = len(u.iterdir()) == len(c.iterdir())

class Arm:
    # Class initialization
    def __init__(self):
        self.ACTION = 0
        self.STATUS = 0

    # Send action command to Arduino
    def SendAction(self):
        pass

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

# Connect to arm

# Begin main loop
# while True:
    # Update flags

    # Display GUI

    # Run frame saving (if needed)

    # Run compression algorithm (if needed)

    # Run transmit algorithm (if needed)