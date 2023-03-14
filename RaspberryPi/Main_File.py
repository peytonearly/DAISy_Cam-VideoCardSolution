### Raspberry Pi Main Loop File ###

# Import Python libraries
from pathlib import Path
import cv2
import os
import time

# Import project files
from Flag import FLAG
from GUI import GUI
import Compressing
import Saving
import Transmitting
from Arm_Control import Arm

### Program Launch Initialization ###
flags = FLAG()
arm = Arm()
gui = GUI(flags)

### Program Main Loop ###
