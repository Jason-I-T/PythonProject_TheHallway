from tkinter import *

root = Tk()

photo = PhotoImage(file="Hallway1.png")
label = Label(root, image = photo)
label.pack()

root.mainloop()