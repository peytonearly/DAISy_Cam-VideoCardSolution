## Compression Algorithm Controller ##

from pathlib import Path
import cv2
from Main_Script import FLAG

def Compression(u: Path, c: Path, flags: FLAG):
    # Inputs:
    #   u - Uncompressed folder path
    #   c - Compressed folder path
    #   flags - FLAG class object
    
    # Select next image file to compress
    #   Determine based on last file saved to Compressed folder
    compFiles = sorted([str(x) for x in c.iterdir()]) # Create sorted list of files in Compressed folder
    mostRecent = compFiles[len(compFiles)-1] # Find most recent folder placed in Compressed folder
    uncompEqual = mostRecent[:(len(mostRecent)-11)] + 'U' + str(int(mostRecent[(len(mostRecent)-10):len(mostRecent)-4])+1).zfill(6) + mostRecent[len(mostRecent)-4:]
    if not Path(uncompEqual).exists(): # Break if file hasn't been created yet
        return
    
    # Compress frame
    
    # Save to compressed folder
    
def CompressJPEG2000():
    pass

def CompressH264():
    pass

def CompressH265():
    pass

if __name__ == "__main__":
    ## Testing Code - Delete Later ##
    p = Path(__file__).parent # Set path at current working directory (file folder)
    u = p / 'Uncompressed'
    c = p / 'Compressed'
    flags = FLAG
    Compression(u, c, flags)