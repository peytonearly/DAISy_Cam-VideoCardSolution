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
    # compFiles = sorted()
    
    if not len(compFiles):
        day = date.today().strftime("%m%d") # Find current mmdd
        todayUStr = day + "U000000.png" # Create image name string from date and naming standard
        todayCStr = day + "C000000.png" # Create image name string from date and naming standard
        nextCPath = flags.c / todayCStr
        nextUPath = flags.u / todayUStr
    else:
        currComp = compFiles[len(compFiles)-1] # Find most recent folder placed in Compressed folder
        nextUPath = currComp[len(currComp)-15:(len(currComp)-11)] + 'U' + str(int(currComp[(len(currComp)-10):len(currComp)-4])+1).zfill(6) + currComp[len(currComp)-4:]
        nextCPath = nextUPath[:len(nextUPath)-11] + 'C' + nextUPath[len(nextUPath)-10:]

        # Create paths based on file names
        nextUPath = flags.u / nextUPath
        nextCPath = flags.c / nextCPath

    # Continue if file has been created 
    if Path(nextUPath).exists():

        # Load frame from uncompressed folder
        image = cv2.imread(str(nextUPath))
        
        # Set compression method parameters
        if flags.METHOD == 0: 
            # No compression method
            # params = [cv2.IMWRITE_PNG_STRATEGY_FIXED, flags.COMPQUAL]
            params = []
        elif flags.METHOD == 1: 
            # JPEG2000
            params = [cv2.IMWRITE_JPEG2000_COMPRESSION_X1000, flags.COMPQUAL]
        elif flags.METHOD == 2: 
            # Run-length encoding
            params = [cv2.IMWRITE_PNG_STRATEGY_RLE, flags.COMPQUAL]
        elif flags.METHOD == 3: 
            # Dynamic Huffman encoding
            params = [cv2.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY, flags.COMPQUAL]
        elif flags.METHOD == 4: 
            # Static Huffman encoding
            params = [cv2.IMWRITE_PNG_STRATEGY_FIXED, flags.COMPQUAL]

        # Save compressed image
        cv2.imwrite(str(nextCPath), image, params)
    return

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    flags = FLAG()
    flags.METHOD = 0

    while not flags.EQUAL:
        Compression(flags)
        flags.UpdateFlags()