# Inspired from https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

# Notes:
# Compression doesn't seem to actually be compressing the images properly
#   Look into trying a new technique using PIL since that seemed to work
# When compression is run during stream, fps lags very badly

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
out = cv2.VideoWriter(path+"\\UncompressedLiveVideo.avi", cv2.VideoWriter_fourcc(*'MJPG'), 20, (frame_width, frame_height))
out_comp = cv2.VideoWriter(path+"\\CompressedLiveVideo.avi", cv2.VideoWriter_fourcc(*'MJPG'), 20, (frame_width, frame_height))
print("Video files created.")

while(True):
    ret, frame = cam.read()
    
    if ret:
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # Write uncompressed frame into file
        out.write(frame)
        
        # Convert, compress, and save image
        # pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_YUV2RGB))
        encode_jp2 = [int(cv2.IMWRITE_JPEG2000_COMPRESSION_X1000), 300] # Set jpeg2000 compression ratio to 30%
        res, img_comp = cv2.imencode('.jp2', frame, encode_jp2)
        img_dec = cv2.imdecode(img_comp, cv2.IMREAD_COLOR)
        out_comp.write(img_dec)
        # out_comp.write(frame)
        
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else:
        break

# When everything is finished, release video capture and video write objects
cam.release()
# out.release()
out_comp.release()

# Closes all the frames
cv2.destroyAllWindows()