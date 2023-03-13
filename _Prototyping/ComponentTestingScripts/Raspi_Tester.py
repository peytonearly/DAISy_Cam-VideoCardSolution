import cv2
import numpy as np
from PIL import Image
import os

# Get path of current directory
path = os.path.dirname(os.path.abspath(__file__))

# Create video capture object
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Unable to open camera. Exiting program.")
    exit()
    
