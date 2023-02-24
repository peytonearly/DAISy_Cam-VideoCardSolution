import tkinter as tk

class GUI:
    def __init__(self):
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
        self.master = tk.Tk()
        self.master.title("DAISy Cam Video Control Interface")
        self.master.geometry('{}x{}'.format(700, 500))
        
        # Create main sections
        self.vidCtrlFrame = tk.Frame(self.master, bg='gray', width=150, height=150, padx=3, pady=3)
        self.compFrame = tk.Frame(self.master, bg='blue', width=150, height=150, padx=3, pady=3)
        self.armFrame = tk.Frame(self.master, bg='green', width=200, height=150, padx=3, pady=3)
        self.camFrame = tk.Frame(self.master, bg='yellow', width=300, height=300, padx=3, pady=3)
        self.statFrame = tk.Frame(self.master, bg='orange', width=200, height=300, padx=3, pady=3)
        self.consoleFrame = tk.Frame(self.master, bg='red', width=200, height=500, padx=3, pady=3)
        
        # Layout main sections
        self.vidCtrlFrame.grid(row=0, column=0, rowspan=2, sticky='nesw')
        self.compFrame.grid(row=0, column=1, rowspan=2, sticky='nesw')
        self.armFrame.grid(row=0, column=2, columnspan=2, rowspan=2, sticky='nesw')
        self.camFrame.grid(row=2, column=0, columnspan=3, rowspan=3, sticky='nesw')
        self.statFrame.grid(row=2, column=2, columnspan=2, rowspan=3, sticky='nesw')
        self.consoleFrame.grid(row=0, column=3, columnspan=2, rowspan=5, sticky='nesw')
    
if __name__ == "__main__":
    gui = GUI()
    gui.InitializeGUI()
    gui.master.mainloop()