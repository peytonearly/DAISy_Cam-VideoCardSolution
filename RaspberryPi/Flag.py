# Import Python libraries
from pathlib import Path
import os

class FLAG:
    # Class initialization
    def __init__(self):
        # Set flags
        self.RECORD   = 0  # 1 if recording video
        self.TRANSMIT = 0  # 1 if ready to transmit video files
        self.FOLDER   = 0  # 1 if files are present in the uncompressed image folder
        self.EQUAL    = 0  # 1 if same number of files in compressed and uncompressed image folders
        self.METHOD   = 0  # 0 for no compression
                           # 1 for JPEG2000
                           # 2 for Run-length encoding
                           # 3 for Dynamic Huffman encoding
                           # 4 for Static Huffman encoding
        self.ACTIVE   = 0  # 1 if compression algorithm is running
        self.COMPQUAL = 60 # Compression quality (x % of original quality)
        self.ARMCMD   = 0  # 0 for arm stopped
                           # 1 for moving arm toward fully opened
                           # 2 for moving arm toward fully closed
                           # 3 for looping arm between open and closed
        self.FILETYPE = ['*.png', '*.jp2', '*.png', '*.png', '*.png']

        # Serial communication port name
        self.COMNAME  = '/dev/serial0'

        # Create compressed/uncompressed directories
        self.p = Path(__file__).parent # Set path at current working directory (cwd)
        self.u = self.p / 'Uncompressed'
        self.c = self.p / 'Compressed'
        self.d = self.p / 'Decompressed'
        self.v = self.p / 'Videos'
        # self.RemoveDirectories() # Comment out if using Windows system
        self.CreateDirectories()
    
    def RemoveDirectories(self):
        # Remove image directories on launch
        os.system("rm -r {} {} {} {}".format(str(self.u), str(self.c), str(self.d), str(self.v)))
    
    def CreateDirectories(self):
        # Create image directories if they don't yet exist
        if not self.u.exists():
            self.u.mkdir(parents=True, exist_ok=False)
        if not self.c.exists():
            self.c.mkdir(parents=True, exist_ok=False)
        if not self.d.exists():
            self.d.mkdir(parents=True, exist_ok=False)
        if not self.v.exists():
            self.v.mkdir(parents=True, exist_ok=False)
    
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

    # Check if there are any files in the compressed image folder
    def CheckCompressedFolder(self):
        return any(list(self.c.glob(self.FILETYPE[self.METHOD])))

    # Check if equal flag should be updated
    def CheckEqual(self):
        self.EQUAL = len(list(self.u.glob('*.png'))) == len(list(self.c.glob(self.FILETYPE[self.METHOD])))

    # Returns a sorted list of uncompressed file names
    def GetSortedFilesUncompressed(self):
        return sorted([str(x) for x in self.u.iterdir()])
    
    # Returns a sorted list of compressed file names
    def GetSortedFilesCompressed(self):
        return sorted([str(x) for x in self.c.iterdir()])
    
    # Returns a sorted list of decompressed file names
    def GetSortedFilesDecompressed(self):
        return sorted([str(x) for x in self.d.iterdir()])
    
    # Returns a sorted list of video file names
    def GetSortedVideoFiles(self):
        return sorted([str(x) for x in self.v.iterdir()])