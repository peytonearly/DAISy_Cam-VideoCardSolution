### Testing Scripts File ###
# Contains functions for testing and validation

# Import Python libraries
from pathlib import Path
from PIL import Image
import numpy as np
from collections import Counter
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Set environment variable to hide Pygame welcome message
import pygame

# Import custom libraries
from Flag import FLAG

# Find compression codecs discovered in Compressed images folder
def GetCompCodecs(flags: FLAG):
    codecs = [] # Initialize array
    files = sorted([str(x) for x in flags.c.iterdir()]) # Create sorted list of files in compressed folder
    for file in files:
        codec = Image.open(file).format
        if codec not in codecs:
            codecs.append(codec)
    return codecs

# Returns the 5 most frequent color codes
def GetRGBValues(flags: FLAG):
    vals = [] # Initialize array
    files = sorted([str(x) for x in flags.u.iterdir()]) # Create sorted list of files in uncompressed folder

    print("Collecting pixel values.")

    # Collect 5 most common pixel values from each image in uncompressed folder
    for file in files:
        im = Image.open(file)
        imArr = np.array(im)
        pixelVals = (imArr[:, :, 0] + imArr[:, :, 1]*256 + imArr[:, :, 2]*(256**2)).flatten()
        count = Counter(pixelVals)
        vals.append(count.most_common(5))

    print("Restructuring into dictionary.")

    # Restructure values
    valsDict = {}
    loopLength = 100 if len(vals)>1000 else len(vals)
    for im in range(loopLength):
        for px in range(5):
            # Check if key exists in dictionary
            if vals[im][px][0] in valsDict.keys():
                valsDict[vals[im][px][0]] += vals[im][px][1]
            else:
                valsDict[vals[im][px][0]] = vals[im][px][1]
    
    # Sort values
    valsDict = dict(sorted(valsDict.items(), reverse=True, key=lambda item: item[1]))

    print("Converting to RGB.")

    # Convert values to RGB
    valsRGB = []
    for val in valsDict:
        r, g, b = val%256, (val//256)%256, val//(256**2)
        valsRGB.append([[r,g,b], valsDict[val]])

    return valsRGB

def DisplayRGB(RGB):
    pygame.init()                          # Initialize Pygame
    size = (400, 400)                      # Set window size
    color = (RGB[0], RGB[1], RGB[2])       # Put RGB array into touple
    screen = pygame.display.set_mode(size) # Create Pygame window
    screen.fill(color)                     # Fill the window with color
    pygame.display.flip()                  # Update the display

    # Loop until window is closed
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
    
    # Quit Pygame
    pygame.quit()

# Debugging section
if __name__ == "__main__":
    flags = FLAG()

    # codecs = GetCompCodecs(flags)
    # print(codecs)

    vals = GetRGBValues(flags)
    for val in vals[:5]:
        print("RGB -> ", val[0])
        DisplayRGB(val[0])
