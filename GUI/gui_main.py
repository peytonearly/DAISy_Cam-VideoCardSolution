import tkinter as tk

# create the main window
root = tk.Tk()

# create a canvas to draw on
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# draw a box on the canvas

# Create main box
box = canvas.create_rectangle(1000, 1000, 0, 0, fill='grey')

# Create deploy arm button
button_deploy_arm = canvas.create_rectangle(10,100,210,150,fill = 'green')


# Create retract arm button
button_retract_arm = canvas.create_rectangle(10,200,210,252,fill = 'yellow')

# Create stop arm button
button_stop_arm = canvas.create_rectangle(10,300,210,352,fill = 'red')

# Create compression selection button
button_compress_select= canvas.create_rectangle(250,100,750,150,fill = 'purple')

# Create start recording button
button_start_record = canvas.create_rectangle(790,100,990,150,fill = 'green')

# Create transfer recording button
button_transfer_record = canvas.create_rectangle(790,200,990,252,fill = 'yellow')

# Create stop video button
button_stop_record = canvas.create_rectangle(790,300,990,352,fill = 'red')


# Create dialogue box
button_stop_record = canvas.create_rectangle(250,300,750,352,fill = 'indigo')


#Create live camera video feed
button_live_feed = canvas.create_rectangle(0,1000,500,500,fill = 'magenta')



# Create two graphs

button_live_feed = canvas.create_rectangle(0,1000,500,500,fill = 'magenta')

button_live_feed = canvas.create_rectangle(500,1000,1000,500,fill = 'cyan')


# run the main loop
root.mainloop()