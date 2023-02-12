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
# cam = cv2.VideoCapture(1)
cam = cv2.VideoCapture(path + "\\Second_Video.mp4")
if not cam.isOpened():
    print("Cannot open camera. Exiting...")
    exit()
    
print("Video initialized. Starting compression...")

# Loop until told to stop
stop = 0
while True:
    stop += 1
    
    # Capture frame-by-frame
    ret, frame = cam.read()
    
    # Check if frame is read correctly
    if not ret:
        print("Error receiving frame. Exiting...")
        # exit()
        break
    
    # Convert opencv image to PIL image
    # color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # color_converted = cv2.cvtColor(frame, cv2.COLOR_BayerRG2RGB) # Camera captures video in RGB Bayer pattern
    # color_converted = cv2.cvtColor(frame, cv2.COLOR_YUV420sp2RGB) # Video might actually be YUV format
    # pil_image = Image.fromarray(color_converted)
    pil_image = Image.fromarray(frame)
    
    # Compress and save
    pil_image.save(path+"\\CompressedImages\\Frame"+str(stop)+"_Compressed.jpg", optimize=True, quality=30)
    # cv2.imwrite(path+"\\UncompressedImages\\Frame"+str(stop)+".jpg", color_converted)
    cv2.imwrite(path+"\\UncompressedImages\\Frame"+str(stop)+".jpg", frame)
    
    # if stop >= 500:
    #     break

# Release the capture when finished
cam.release()
cv2.destroyAllWindows()

print("Compression finished. Converting to videos...")

# Recompile images into videos
img_array = []
filenames = []
repeats = 0
for filename in glob.glob(path+"\\UncompressedImages\\*.jpg"):
    if filename in filenames:
        repeats += 1
    filenames.append(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    
print(repeats)

comp_img_array = []
filenames_comp = []
repeats_comp = 0
for filename in glob.glob(path+"\\CompressedImages\\*.jpg"):
    if filename in filenames_comp:
        repeats_comp += 1
    filenames_comp.append(filename)
    img = cv2.imread(filename)
    height_comp, width_comp, layers_comp = img.shape
    size_comp = (width_comp, height_comp)
    comp_img_array.append(img)

print(repeats_comp)
    
out = cv2.VideoWriter(path+"\\UncompressedVideo.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

out_comp = cv2.VideoWriter(path+"\\CompressedVideo.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, size_comp)
for i in range(len(comp_img_array)):
    out_comp.write(comp_img_array[i])
out_comp.release()