# Video Compression Code
# Date: 11/1/2022
# Take in Images frame by frame and Compress by a Certain Factor
import math
import PIL
from PIL import Image
import cv2
import pandas as pd

vidcap = cv2.VideoCapture('Real_Slim_Shady.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("Compressed_Images_Folder/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  scale_percent = 60 # percent of original size
  width = int(image.shape[1] * scale_percent / 100)
  height = int(image.shape[0] * scale_percent / 100)
  dim = (width, height)
  #resize image
  resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
  print('Read a new frame: ', success)
  count += 1