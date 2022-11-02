# Inspired from https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

import cv2
import numpy as np
from PIL import Image
import os

# Get path of current directory
path = os.path.dirname(os.path.abspath(__file__))

# Create VideoCapture object
cam = cv2.VideoCapture(1)

if not cam.isOpened():
    print("Unable to open camera. Exiting program.")
    exit()
    
# Integer representations of width and height
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))

# Define VideoWriter object for compressed and uncompressed
out = cv2.VideoWriter(path+"\\UncompressedLiveVideo.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))
out_comp = cv2.VideoWriter(path+"\\CompressedLiveVideo.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))

while(True):
    ret, frame = cam.read()
    
    if ret:
        # Write uncompressed frame into file
        out.write(frame)
        
        # Convert, compress, and save image
        pil_image