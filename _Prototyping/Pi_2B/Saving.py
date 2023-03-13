## Image Saving Algorithm Controller ##
from pathlib import Path
import cv2
from Main_Script import FLAG

def Saving(flags: FLAG, im):
    # Inputs:
    #   flags - Instance of FLAG class
    #   im  - OpenCV image object
    #   u   - Uncompressed folder path object
    
    flags.CheckFolder()

    # Save current frame to uncompressed folder with appropriate naming format
    if not flags.FOLDER:
        # Create file name if first image in folder
        nextFileName = flags.u / '0309U000000.png'
    else:
        uncompFiles = sorted([str(x) for x in flags.u.iterdir()])
        mostRecent = uncompFiles[len(uncompFiles)-1]
        nextFileName = mostRecent[:(len(mostRecent)-10)] + str(int(mostRecent[(len(mostRecent)-10):len(mostRecent)-4])+1).zfill(6) + mostRecent[len(mostRecent)-4:]

    # Save image with openCV
    cv2.imwrite(str(nextFileName), im)

if __name__ == "__main__":
    flags = FLAG()

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Camera failed to open.")
        exit()
    
    for i in range(100):
        ret, frame = cam.read()

        if ret:
            Saving(flags, frame)