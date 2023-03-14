# Import Python Libraries
from pathlib import Path
import cv2
import os
from datetime import date

# Import custom files
from Flag import FLAG

def Compression(flags: FLAG):
    # Inputs:
    #   flags - FLAG class object
    
    # Select next image file to compress
    #   Determine based on last file saved to Compressed folder
    compFiles = sorted([str(x) for x in flags.c.iterdir()]) # Create sorted list of files in Compressed folder
    if not len(compFiles):
        day = date.today().strftime("%m%d") # Find current mmdd
        todayUStr = day + "U000000.png" # Create image name string from date and naming standard
        todayCStr = day + "U000000.png" # Create image name string from date and naming standard
        nextComp = flags.c / todayCStr
        uncompNext = flags.u / todayUStr
    else:
        mostRecent = compFiles[len(compFiles)-1] # Find most recent folder placed in Compressed folder
        uncompNext = mostRecent[len(mostRecent)-15:(len(mostRecent)-11)] + 'U' + str(int(mostRecent[(len(mostRecent)-10):len(mostRecent)-4])+1).zfill(6) + mostRecent[len(mostRecent)-4:]
        nextComp = uncompNext[:len(uncompNext)-11] + 'C' + uncompNext[len(uncompNext)-10:]

        # Create paths based on file names
        uncompNext = flags.u / uncompNext
        nextComp = flags.c / nextComp

        # Break if file hasn't been created yet
        if not Path(uncompNext).exists():
            return

    # Load frame from uncompressed folder
    image = cv2.imread(str(uncompNext))
    
    # Set compression method parameters
    if not flags.METHOD: # No compression method
        # params = [cv2.IMWRITE_PNG_STRATEGY_FIXED, flags.COMPQUAL]
        params = []
    elif flags.METHOD == 1: # JPEG2000
        params = [cv2.IMWRITE_JPEG2000_COMPRESSION_X1000, flags.COMPQUAL]
    elif flags.METHOD == 2: # Run-length encoding
        params = [cv2.IMWRITE_PNG_STRATEGY_RLE, flags.COMPQUAL]
    elif flags.METHOD == 3: # Dynamics Huffman encoding
        params = [cv2.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY, flags.COMPQUAL]
    elif flags.METHOD == 4: # Static Huffman encoding
        params = [cv2.IMWRITE_PNG_STRATEGY_FIXED, flags.COMPQUAL]

    # Save compressed image
    cv2.imwrite(str(nextComp), image, params)

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    flags = FLAG()
    flags.METHOD = 0

    while not flags.EQUAL:
        Compression(flags)
        flags.UpdateFlags()