# Inspired from https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

import cv2
import numpy as np
from PIL import Image
import os

# Get path of current directory
path = os.path.dirname(os.path.abspath(__file__))

# Create VideoCapture object
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Unable to open camera. Exiting program.")
    exit()
    
# Integer representations of width and height
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))

# Define VideoWriter object for compressed and uncompressed
out = cv2.VideoWriter(path+"\\UncompressedLiveVideo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20, (frame_width, frame_height))
out_comp = cv2.VideoWriter(path+"\\CompressedLiveVideo.mp4", cv2.VideoWriter_fourcc(*'mpv4'), 20, (frame_width, frame_height))

while(True):
    ret, frame = cam.read()
    
    if ret:
        # Write uncompressed frame into file
        out.write(frame)
        
        # Convert, compress, and save image
        # pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_YUV2RGB))
        out_comp.write(frame)
        
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else:
        break

# When everything is finished, release video capture and video write objects
cam.release()
out.release()
out_comp.release()

# Closes all the frames
cv2.destroyAllWindows()