import tkinter as tk
from tkinter import ttk
class Taskbar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='gray')
        self.is_recording = False
        self.style = ttk.Style()
        self.style.configure('Record.TButton', foreground='black', background='#F7F7F7', font=('TkDefaultFont', 12, 'bold'), borderwidth=0)
        self.style.map('Record.TButton', background=[('pressed', 'gray')], relief=[('pressed', 'sunken')])
        self.record_button = ttk.Button(self, text="Record", style='Record.TButton', command=self.toggle_recording)
        self.record_button.pack(side='right', padx=10, pady=5)
    def toggle_recording(self):
        if self.is_recording:
            self.style.configure('Record.TButton', foreground='black', background='#F7F7F7')
            self.record_button.configure(text='Record')
        else:
            self.style.configure('Record.TButton', foreground='black', background='#F7F7F7')
            self.record_button.configure(text='Stop')
        self.is_recording = not self.is_recording
class TelemetryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='green')
class VideoFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.red_box = tk.Canvas(self, width=400, height=300, bg='red')
        self.red_box.pack(side='left', padx=10, pady=10, anchor='sw')
        self.purple_box = tk.Canvas(self, width=400, height=300, bg='purple')
        self.purple_box.pack(side='left', padx=10, pady=10, anchor='sw')

class ImageFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.blue_box = tk.Canvas(self, width=200, height=300, bg='blue')
        self.blue_box.pack(side='bottom', padx=10, pady=10, anchor='se')

        # Create four canvas widgets for each quadrant
        self.top_left = tk.Canvas(self.blue_box, width=400, height=150, bg='brown')
        self.top_right = tk.Canvas(self.blue_box, width=400, height=150, bg='gray')
        self.bottom_left = tk.Canvas(self.blue_box, width=400, height=150, bg='black')
        self.bottom_right = tk.Canvas(self.blue_box, width=400, height=150, bg='red')

        # Place each quadrant in the appropriate location within the blue_box canvas
        self.blue_box.create_window(0, 0, anchor='nw', window=self.top_left)
        self.blue_box.create_window(400, 0, anchor='nw', window=self.top_right)
        self.blue_box.create_window(0, 150, anchor='nw', window=self.bottom_left)
        self.blue_box.create_window(400, 150, anchor='nw', window=self.bottom_right)
class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.state('zoomed')
        self.master.title("My Window")
        self.taskbar = Taskbar(self.master)
        self.taskbar.pack(fill='x', side='top')
        self.telemetry_frame = TelemetryFrame(self.master)
        self.telemetry_frame.pack(fill='both', expand=True)
        self.frame = tk.Frame(self.master)
        self.frame.pack(side='left', fill='both', expand=True)
        self.video_frame = VideoFrame(self.frame)
        self.video_frame.pack(side='left', fill='both', expand=True)
        self.image_frame = ImageFrame(self.frame)
        self.image_frame.pack(side='left', fill='both', expand=True)
if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    app.mainloop()