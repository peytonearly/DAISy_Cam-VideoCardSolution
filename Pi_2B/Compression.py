## Compression Algorithm Controller ##

# Compression Algorithms:
#   0 - None
#       IMWRITE_PNG_STRATEGY_DEFAULT
#   1 - JPEG2000
#       IMWRITE_JPEG2000_COMPRESSION_X1000
#   2 - Run-length encoding
#       IMWRITE_PNG_STRATEGY_RLE or IMWRITE_EXR_COMPRESSION_RLE
#   3 - Huffman encoding (dynamics and static)
#       IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY
#       IMWRITE_PNG_STRATEGY_FIXED

# Compressing
#   cv2.imwrite()

# Decompressing
#   cv2.imdecode()

from pathlib import Path
import cv2
from Main_Script import FLAG
import os

def Compression(flags: FLAG):
    # Inputs:
    #   flags - FLAG class object
    
    # Select next image file to compress
    #   Determine based on last file saved to Compressed folder
    compFiles = sorted([str(x) for x in flags.c.iterdir()]) # Create sorted list of files in Compressed folder
    if not len(compFiles):
        nextComp = flags.c / '0309C000000.png'
        uncompNext = flags.u / '0309U000000.png'
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
    if not flags.METHOD:
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
        # Dynamics Huffman encoding
        params = [cv2.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY, flags.COMPQUAL]
    elif flags.METHOD == 4:
        # Static Huffman encoding
        params = [cv2.IMWRITE_PNG_STRATEGY_FIXED, flags.COMPQUAL]

    # Save compressed image
    cv2.imwrite(str(nextComp), image, params)

def RemoveDirectories(flags: FLAG):
    os.system("rmdir /s " + str(flags.c))

if __name__ == "__main__":
    ## Testing Code - Delete Later ##
    flags = FLAG()
    flags.METHOD = 0

    RemoveDirectories(flags)

    # while not flags.EQUAL:
    #     Compression(flags)
    #     flags.UpdateFlags()