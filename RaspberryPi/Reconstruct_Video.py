# Import libraries
import cv2
from pathlib import Path

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

if __name__ == "__main__":
    flags = FLAG()
    flags.METHOD = 1
    flags.CreateDirectories()
    flags.UpdateFlags()

    fourcc_codes = [
        'MP42',
        'MJPG',
        'MJ2C',
        'HEVC',
        'X264'
    ]

    video_filenames = [
        "MPEG4",
        "MotionJPEG",
        "MotionJPEG2000",
        "H265",
        "H264"
    ]

    video_extensions = [
        ".mp4v",
        ".mp4v",
        ".mj2",
        ".hev1",
        ".avc1"
    ]

    video_method = [
        "Video_U_",
        "Video_C_"
    ]

    size = (640, 360)

    # videoName = "Video_U_" + video_filenames[0] + video_extensions[0]
    # videoPath = flags.v / videoName
    # print(videoPath)

    uncompFiles = flags.GetSortedFilesUncompressed()
    compFiles = flags.GetSortedFilesCompressed()

    # if flags.EQUAL: # Only run if all images have been compressed
    #     for j in range(len(fourcc_codes)): # Each codec
    #         # Uncompressed file
    #         filenameU = video_method[0] + video_filenames[j] + video_extensions[j]
    #         filepathU = flags.v / filenameU

    #         # Compressed file
    #         filenameC = video_method[1] + video_filenames[j] + video_extensions[j]
    #         filepathC = flags.v / filenameC

    #         # Create video objects
    #         videoU = cv2.VideoWriter(str(filepathU), cv2.VideoWriter_fourcc(fourcc_codes[j][0], fourcc_codes[j][1], fourcc_codes[j][2], fourcc_codes[j][3]), 30, size)
    #         videoC = cv2.VideoWriter(str(filepathC), cv2.VideoWriter_fourcc(fourcc_codes[j][0], fourcc_codes[j][1], fourcc_codes[j][2], fourcc_codes[j][3]), 30, size)

    #         for f in range(len(uncompFiles)):
    #             videoU.write(cv2.imread(uncompFiles[f]))
    #             videoC.write(cv2.imread(compFiles[f]))
            
    #         videoU.release()
    #         videoC.release()

    # name = "TestVideo_AVC1.mp4"
    name = "TestVideo_H264.avi"
    nPath = flags.v / name
    # video = cv2.VideoWriter(str(nPath), cv2.VideoWriter_fourcc('a', 'v', 'c', '1'), 30, size)
    video = cv2.VideoWriter(str(nPath), cv2.VideoWriter_fourcc('H', '2', '6', '4'), 30, size)
    for im in uncompFiles:
        video.write(cv2.imread(im))
    video.release()

# TO DO
# Save uncompressed images into .mp4 with avc1 codec
# Use ffmpeg command to save into .mp4 with H264 (commandline)