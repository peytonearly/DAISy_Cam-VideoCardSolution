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
        self.red_box.pack(side='left', padx=10, pady=10, anchor='se')
        self.purple_box = tk.Canvas(self, width=400, height=300, bg='purple')
        self.purple_box.pack(side='left', padx=10, pady=10, anchor='sw')

class ImageFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.yellow_box = tk.Canvas(self, width=100, height=150, bg='yellow')
        self.yellow_box.pack(side='left', padx=10, pady=10, anchor='sw')
        self.brown_box = tk.Canvas(self, width=100, height=150, bg='brown')
        self.brown_box.pack(side='left', padx=10, pady=10, anchor='sw')
        self.pink_box = tk.Canvas(self, width=100, height=150, bg='pink')
        self.pink_box.pack(side='left', padx=10, pady=10, anchor='sw')
        self.grey_box = tk.Canvas(self, width=100, height=150, bg='grey')
        self.grey_box.pack(side='left', padx=10, pady=10, anchor='sw')
        self.orange_box = tk.Canvas(self, width=100, height=150, bg='orange')
        self.orange_box.pack(side='left', padx=10, pady=10, anchor='sw')
        
        





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