# CompressionTest_Computer.py
# This file captures video from the camera and saves a compressed and uncompressed copy

import cv2
from PIL import Image
import numpy as np
import glob
import os

# Get path of current directory
path = os.path.dirname(os.path.abspath(__file__))

# Initialize camera video capture
cam = cv2.VideoCapture(1)
if not cam.isOpened():
    print("Cannot open camera. Exiting...")
    exit()

# Loop until told to stop
stop = 0
while True:
    stop += 1
    
    # Capture frame-by-frame
    ret, frame = cam.read()
    
    # Check if frame is read correctly
    if not ret:
        print("Error receiving frame. Exiting...")
        exit()
    
    # Convert opencv image to PIL image
    color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(color_converted)
    
    # Compress and save
    pil_image.save(path+"\\CompressedImages\\Frame"+str(stop)+"_Compressed.jpg", optimize=True, quality=30)
    cv2.imwrite(path+"\\UncompressedImages\\Frame"+str(stop)+".jpg", color_converted)
    
    if stop >= 200:
        break

# Release the capture when finished
cam.release()
cv2.destroyAllWindows()

# Recompile images into videos
img_array = []
for filename in glob.glob(path+"\\UncompressedImages\\*.jpg"):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

comp_img_array = []
for filename in glob.glob(path+"\\CompressedImages\\*.jpg"):
    img = cv2.imread(filename)
    height_comp, width_comp, layers_comp = img.shape
    size_comp = (width_comp, height_comp)
    comp_img_array.append(img)
    
out = cv2.VideoWriter(path+"UncompressedVideo.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

out_comp = cv2.VideoWriter(path+"CompressedVideo.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(comp_img_array)):
    out_comp.write(comp_img_array[i])
out_comp.release()