# Import Python libraries
import tkinter as tk

# Import custom functions
from Flag import FLAG

# GUI class
class GUI: # NEEDS REWORK #
    def __init__(self, flags: FLAG):
        self.CompressionMethod = 0 # 0 for none
                                   # 1 for JPEG200
                                   # 2 for H.264
                                   # 3 for H.265
        self.ArmMove = 0 # 0 for retracting arm
                         # 1 for deploying arm
                         # 2 for looping arm
        self.Stop = 0 # 1 if stop arm movement
        self.Record = 0 # 1 if recording video
    
    def StopArm(self):
        pass

    def UpdateArmMovement(self, val):
        if val == 0: # Close arm
            self.ArmMove = 0
        elif val == 1: # Open arm
            self.ArmMove = 1
        elif val == 2: # Loop
            self.ArmMove = 2

    def UpdateCompMethods(self, selection):
        if selection > 0 and selection < 4: # Only update flag if value is within expected values
            self.CompressionMethod = selection

    def UpdateRecord(self):
        if self.Record:
            self.Record = 0
        else:
            self.Record = 1
            
    def InitializeGUI(self):
        # Create master window        
        # Create main sections        
        # Layout main sections
        pass

### Testing ###
# Will run if this file is called #
if __name__ == "__main__":
    pass