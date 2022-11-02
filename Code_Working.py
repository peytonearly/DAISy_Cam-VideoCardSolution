# Video Compression Code
# Date: 11/1/2022
# Take in Images frame by frame and Compress by a Certain Factor
import math
import PIL
from PIL import Image
import cv2
import pandas as pd
import glob

vidcap = cv2.VideoCapture('Real_Slim_Shady.mp4')
cam = cv2.VideoCapture(1)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("Compressed_Images_Folder/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  if not success:
    break
  scale_percent = 60 # percent of original size
  width = int(image.shape[1] * scale_percent / 100)
  height = int(image.shape[0] * scale_percent / 100)
  dim = (width, height)
  #resize image
  resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
  #print('Read a new frame: ', success)
  count += 1

comp_img_array = []
filenames_comp = []
repeats_comp = 0


for filename in glob.glob("Compressed_Images_Folder\\*.jpg"):
    if filename in filenames_comp:
        repeats_comp += 1
    filenames_comp.append(filename)
    img = cv2.imread(filename)
    height_comp, width_comp, layers_comp = img.shape
    size_comp = (width_comp, height_comp)
    comp_img_array.append(img)
out_comp = cv2.VideoWriter("FuckKanye5.mp4v", cv2.VideoWriter_fourcc('m','p','4','v'), 120, size_comp)
for i in range(len(comp_img_array)):
    out_comp.write(comp_img_array[i])
out_comp.release()