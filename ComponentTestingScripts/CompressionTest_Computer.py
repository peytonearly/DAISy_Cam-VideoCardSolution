# CompressionTest_Computer.py
# This file tests the compression algorithm using the local machine
# Must have pillow library installed (pip install pillow)
# Must have opencv library installed (pip install opencv-python)

from PIL import Image
import PIL
import cv2
import os

filename = 'frame1124-Compressed.jpg'
picture = Image.open('frame1124.jpg')
dim = picture.size
print(f"{dim}")
picture.save("Compressed_"+filename, optimize=True, quality=30)