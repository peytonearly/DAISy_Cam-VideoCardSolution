import tkinter

master=tkinter.Tk()
master.title("Arm GUI")
master.geometry("1000x500")

# Deploy arm
button1=tkinter.Button(master, text="Deploy Arm")
button1.place(x=25, y=25,height=50, width=200)

#Stop Arm
button2=tkinter.Button(master, text="Retract Arm")
button2.place(x=25, y=100,height=50, width=200)

#Stop Arm
button3=tkinter.Button(master, text=" Stop Arm ")
button3.place(x=25, y=175,height=50, width=200)

########################################################################################
# Start Recording
button4=tkinter.Button(master, text="Start Recording")
button4.place(x=775, y=25,height=50, width=200)

# Transfer Recording
button5=tkinter.Button(master, text="Retract Arm")
button5.place(x=775, y=100,height=50, width=200)

#Stop Recording
button6=tkinter.Button(master, text=" Stop Arm ")
button6.place(x=775, y=175,height=50, width=200)

##############################################################################################
 # Compression Selection
button7=tkinter.Button(master, text="Compression Selection")
button7.place(x=335, y=25,height=50, width=300)

# Dialogue Box
button7=tkinter.Button(master, text="Dialogue Box")
button7.place(x=335, y=175,height=50, width=300)




master.mainloop()