import tkinter as tk

class GUI:
    def __init__(self):
        self.CompressionMethod = 0 # 0 for none
                                   # 1 for JPEG200
                                   # 2 for H.264
                                   # 3 for H.265
        self.ArmMove = 0 # 0 for retracting arm
                         # 1 for deploying arm
        self.Stop = 0 # 1 if stop arm movement
        self.Record = 0 # 1 if recording video
    
    def StopArm(self):
        pass

    def UpdateArmMovement(self):
        if self.ArmMove:
            self.ArmMove = 0
        else:
            self.ArmMove = 1

    def UpdateCompMethods(self, selection):
        if selection > 0 and selection < 4: # Only update flag if value is within expected values
            self.CompressionMethod = selection

    def UpdateRecord(self):
        if self.Record:
            self.Record = 0
        else:
            self.Record = 1

master=tk.Tk()
master.title("Arm GUI")
master.geometry("1000x500")

# Deploy arm
button1=tk.Button(master, text="Deploy Arm")
button1.place(x=25, y=25,height=50, width=200)

#Stop Arm
button2=tk.Button(master, text="Retract Arm")
button2.place(x=25, y=100,height=50, width=200)

#Stop Arm
button3=tk.Button(master, text=" Stop Arm ")
button3.place(x=25, y=175,height=50, width=200)

########################################################################################
# Start Recording
button4=tk.Button(master, text="Start Recording")
button4.place(x=775, y=25,height=50, width=200)

# Transfer Recording
button5=tk.Button(master, text="Retract Arm")
button5.place(x=775, y=100,height=50, width=200)

#Stop Recording
button6=tk.Button(master, text=" Stop Arm ")
button6.place(x=775, y=175,height=50, width=200)

##############################################################################################
 # Compression Selection
button7=tk.Button(master, text="Compression Selection")
button7.place(x=335, y=25,height=50, width=300)

compMethods = ('None', 'JPEG2000', 'H.264', 'H.265')
var = tk.Variable(value=compMethods)
listbox = tk.Listbox(master, height=25)

# Dialogue Box
button7=tk.Button(master, text="Dialogue Box")
button7.place(x=335, y=175,height=50, width=300)




master.mainloop()