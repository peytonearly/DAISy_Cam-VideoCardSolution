### From https://www.geeksforgeeks.org/python-grid-method-in-tkinter/ ##

# Added by me to get it to work with any device
from pathlib import Path
import 

# Import tkinter module
import tkinter as tk

# Create main tkinter window
master = tk.Tk()

# Create label widgets
l1 = tk.Label(master, text = "Height")
l2 = tk.Label(master, text = "Width")

# grid arranges using rows/columns
l1.grid(row=0, column=0, sticky = 'w', pady=2)
l2.grid(row=1, column=0, sticky = 'w', pady=2)

# Create user entry widgets
e1 = tk.Entry(master)
e2 = tk.Entry(master)

# Arrange user entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, columm=1, pady=2)

# Create checkbutton widget
c1 = tk.Checkbutton(master, text="Preserve")
c1.grid(row=1, column=1, pady=2)

# Add image
path = Path(__file__).parent 
path = path / 'kermit dab.png'
img = tk.PhotoImage(str(path))
img1 = img.subsample(2,2)

# Setting image using a label
tk.Label(master, image=img1).grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

# Create button widget
b1 = tk.Button(master, text="Zoom in")
b2 = tk.Button(master, text="Zoom out")

# Arranging button widgets
b1.grid(row=2, column=2, sticky = 'e')
b2.grid(row=2, column=3, sticky = 'e')

master.mainloop()