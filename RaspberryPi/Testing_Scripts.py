### Testing Scripts File ###
# Contains functions for testing and validation

# Import Python libraries
from pathlib import Path
from PIL import Image
import numpy as np
import imghdr
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

    print("Searching for codecs.")

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

    print("==> Restructuring into dictionary.")

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

    print("==> Converting to RGB.")

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

def similarity_func(image_a,image_b):
    # Load the images
    img1 = cv2.imread('image1.jpg')
    img2 = cv2.imread('image2.jpg')

    # Resize the images to the same size (optional)
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))

    # Calculate the MSE between the two images
    mse = np.mean((img1 - img2) ** 2)

    # Calculate the percentage similarity between the two images
    percentage_similarity = (1 - mse / 255 ** 2) * 100
    
    return percentage_similarity    

# Debugging section
if __name__ == "__main__":
    flags = FLAG()

    # codecs = GetCompCodecs(flags)
    # print("==> Found codecs: ")
    # print(codecs)

    # vals = GetRGBValues(flags)
    # for val in vals[:5]:
    #     print("RGB -> ", val[0])
    #     DisplayRGB(val[0])

    # Rating Compression Script

    # Uncompressed (UC)
    # Compressed (C)
    # Decompressed (DC) 

    #UC vs DC
    #UC vs C
    # UC vs DC
    UC_list = {}
    DC_list = {}
    C_list = {}

   C_files = flags.GetSortedFilesUncompressed()
   path_C = flags.c

   UC_files = flags.GetSortedFilesUncompressed()
   path_UC = flags.uc

   DC_files =flags.GetSortedFilesDecompressed()
   path_D = flags.d

    # Initiate features of uncompressed
    #for UC_element in UC_images:
    for file_name in UC_files:
        UC = Pic()
        image = cv2.imread(file_name)
        height, width = image.shape[:2]
        UC.height = height
        UC.width = width
        UC.codec = imghdr.what(file_name)
        file_path = os.path.join(path_UC, file_name)
        UC.filesize = os.path.getsize(file_path)
        UC_list.append(UC)

    # Initiate features of compressed
    for file_name in C_files:
        C = Pic()
        image = cv2.imread(file_name)
        height, width = image.shape[:2]
        C.height = height
        C.width = width
        file_path = os.path.join(path_C, file_name)
        C.codec = imghdr.what(file_name)
        C.filesize = os.path.getsize(file_path)
        C_list.append(C)

    # Initiate features of decompressed
    for file_name in DC_files:
        DC = Pic()
        image = cv2.imread(file_name)
        height, width = image.shape[:2]
        DC.height = height
        DC.width = width
        file_path = os.path.join(path_D, file_name)
        DC.filesize = os.path.getsize(file_path)
        DC.codec = imghdr.what(file_name)
        DC_list.append(DC)


    # C vs UC

    # REQ1: Checking codecs (file format should stay the same)

    # REQ2: Checking number of pixels (lossless so it should be the same)

    A_pixel_hit = 0
    A_codec_hit=  0
    A_fit = 0
    A_miss = 0

    for C_item, UC_item in zip(C_list, UC_list):   

    # Set Flags to be false initially
    codec_val = False
    pixel_val = False

        # Check Codecs
    if (C_item.codec == UC_item.codec):
        codec_val = True
    
    else if (C_item.height == UC_item.height & C_item.width == UC_item.width):
            pixel_val = True

        result = pixel_val & codec_val
    
    if (result == True):
        A_fit+=1
    else:
        if (pixel_val == True & codec_val == False):
            A_pixel_hit+=1
        else if (pixel_val == False & codec_val = True):
            A_codec_hit+=1
        else:
            A_miss+=1

    comp_ratios = {}
    similiarity_ratios = {}

    B_pixel_hit = 0
    B_codec_hit=  0
    B_fit = 0
    B_miss = 0

    for DC_item, UC_item in zip(DC_list, UC_list):   

    # Set Flags to be false initially
    codec_val = False
    pixel_val = False


        # Check Codecs
    if (DC_item.codec == UC_item.codec):
        codec_val = True
    
    else if (DC_item.height == UC_item.height & DC_item.width == UC_item.width):
            pixel_val = True

        result = pixel_val & codec_val
    
    if (result == True):
        B_fit+=1
    else:
        if (pixel_val == True & codec_val == False):
            B_pixel_hit+=1
        else if (pixel_val == False & codec_val = True):
            B_codec_hit+=1
        else:
            B_miss+=1

        # Checking file sizes
        comp_ratios.append(DC_item.filesize/UC_item.filesize)
        similiarity_ratios.append(similarity_func(DC_item,UC_item))