# Import libraries
import cv2
from pathlib import Path
import os

# Import custom files
from Flag import FLAG

### Important fourcc codes ###
# MP42 --> MPEG-4                 | .mp4
# MJPG --> Motion JPEG            | .mp4, .mjpeg
# MJ2C --> Motion JPEG 2000       | .mj2, .mp4, .mjp2
# HEVC --> H.265/HEVC             | .mp4
# HFYU --> Huffman Lossless Codec |
# X264 --> H.264                  | .mp4, .m4v

# Uncompressed videos --> 'avc1' | .mp4
# Compressed videos --> 'h264' | .mp4

def GetImageSize(filename):
    cap = cv2.VideoCapture(filename)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return (width, height)

def CreateVideo(flags: FLAG):
    print("Starting video reconstruction.")
    # Get existing image files
    uncompFiles = flags.GetSortedFilesUncompressed()
    compFiles = flags.GetSortedFilesCompressed()

    # Get image pixel size
    # size = (640, 360)
    size = GetImageSize(uncompFiles[0])

    nameU1 = flags.v / "Video_U_AVC1.mp4"
    # nameU2 = flags.v / "Video_U_H264.mp4"
    nameC1 = flags.v / "Video_C_AVC1.mp4"
    # nameC2 = flags.v / "Video_C_H264.mp4"

    print("Creating fourcc codes.")

    # Initialize fourcc codes
    fcc_mp4v = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # fcc_mp4v = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    # fcc_h264 = cv2.VideoWriter_fourcc('H', '2', '6', '4')

    print("Constructing videos from uncompressed images.")

    # Create videos from uncompressed images
    videoU1 = cv2.VideoWriter(str(nameU1), fcc_mp4v, 30, size)
    # videoU2 = cv2.VideoWriter(str(nameU2), fcc_h264, 30, size)
    for im in uncompFiles:
        videoU1.write(cv2.imread(im))
        # videoU2.write(cv2.imread(im))
    videoU1.release()
    # videoU2.release()

    print("Constructing videos from compressed images.")

    # Create videos from compressed images
    videoC1 = cv2.VideoWriter(str(nameC1), fcc_mp4v, 30, size)
    # videoC2 = cv2.VideoWriter(str(nameC2), fcc_h264, 30, size)
    for im in compFiles:
        videoC1.write(cv2.imread(im))
        # videoC2.write(cv2.imread(im))
    videoC1.release()
    # videoC2.release()

    print("Constructing with ffmpeg.")

    # Use ffmpeg to compressed further
    # ffmpeg -i test.avi -vcodec libx264 test.mp4
    os.system("ffmpeg -i Videos/Video_U_AVC1.mp4 -vcodec libx264 Videos/Video_U_AVC1_FFMPEG.mp4")
    # os.system("ffmpeg -i Videos/Video_U_H264.mp4 -vcodec libx264 Videos/Video_U_H264_FFMPEG.mp4")

    print("Finished video reconstruction.")

if __name__ == "__main__":
    flags = FLAG()
    flags.METHOD = 1
    flags.UpdateFlags()
    CreateVideo(flags)