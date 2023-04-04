### Raspberry Pi Main Loop File ###

# Import Built-In Python libraries
from pathlib import Path
import tkinter as tk
import subprocess
import os
import datetime

# Install required libraries
print("Installing required libraries.")
subprocess.call("Install_Reqs.sh", shell=True)
print("Libraries installed.")

# Import libraries
import cv2
import serial

# Import project files
from Flag import FLAG
from GUI import GUI
from Arm_Control import Arm
from Compressing import Compression
from Saving import SaveFrame
from Transmit_Server import Transmit

### Program Launch Initialization ###
flags = FLAG()
arm = Arm()
gui = GUI(flags)

### Program Main Loop ###
