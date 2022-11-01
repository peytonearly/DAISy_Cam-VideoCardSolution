# ImageExtraction.py
# This file extracts the individual images from the video file and saves them 
# Must have opencv library installed (pip install opencv-python)
# From https://www.geeksforgeeks.org/extract-images-from-video-in-python/

# Known Issues:
#   - For some reason the 'data' folder is ending up in the parent folder for the entire repo........ not sure why

import cv2
import os

# Read the video from the local directory
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "First_Video")
cam = cv2.VideoCapture(filename)

try:
    # Create a folder named data
    if not os.path.exists('ImageData'):
        os.makedirs('ImageData')

# Raise error if file not created
except OSError:
    print('Error: Creating ImageData directory')

# Frame
currentFrame = 0

while(True):
    # Reading from frame
    ret, frame = cam.read()
    
    if ret:
        # If video is still left continue creating images
        name = './ImageData/frame' + str(currentFrame) + '.jpg'
        print('Creating...' + name)
        
        # Writing the extracted images
        cv2.imwrite(name, frame)
        
        # Increment counter
        currentFrame += 1
    else:
        break
    
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()