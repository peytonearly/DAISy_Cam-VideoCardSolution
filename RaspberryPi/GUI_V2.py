import tkinter as tk
from tkinter import ttk

class GUI():
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.geometry("800x600")
        self.master.state('zoomed')
        self.master.title('DAISYCAM GUI')

        # Define button style
        self.style = ttk.Style()
        self.style.configure('Button.TButton', foreground='black', background='#F7F7F7', font=('TkDefaultFont', 12, 'bold'), borderwidth=0)
        self.style.map('Button.TButton', background=[('pressed', 'gray')], relief=['pressed', 'sunken'])

    def createButton(self):
        # Create button variables
        self.boolStop = 1
        self.boolOpen = 0
        self.boolClose = 0
        self.boolLoop = 0
        self.boolRecord = 0

        def toggleStop():
            self.boolStop = not self.boolStop
            if self.boolStop:
                self.buttonStop.configure(text="Stopped")
            else:
                self.buttonStop.configure(text="Stop")

        def toggleOpen():
            self.boolOpen = not self.boolOpen
            if self.boolOpen:
                self.buttonOpen.configure(text="Opening")
            else:
                self.buttonOpen.configure(text="Open")
        
        def toggleClose():
            self.boolClose = not self.boolClose
            if self.boolClose:
                self.buttonClose.configure(text="Closing")
            else:
                self.buttonClose.configure(text="Close")

        def toggleLoop():
            self.boolLoop = not self.boolLoop
            if self.boolLoop:
                self.buttonLoop.configure(text="Looping")
            else:
                self.buttonLoop.configure(text="Loop")
            
        def toggleRecord():
            self.boolRecord = not self.boolRecord
            if self.boolRecord:
                self.buttonRecord.configure(text="Recording")
            else:
                self.buttonRecord.configure(text="Record")

        self.buttonStop = ttk.Button(self, text="Stop Arm", style='Button.TButton', command=toggleStop())
        self.buttonOpen = ttk.Button(self, text="Open Arm", style='Button.TButton', command=toggleOpen())
        self.buttonClose = ttk.Button(self, text="Close Arm", style='Button.TButton', command=toggleClose())
        self.buttonLoop = ttk.Button(self, text="Loop Arm", style='Button.TButton', command=toggleLoop())
        self.buttonRecord = ttk.Button(self, text="Record", style='Button.TButton', command=toggleRecord())

    def createFrames(self, master=None):
        return tk.Frame(master)
    
    def createTaskbar(self, master=None):
        pass