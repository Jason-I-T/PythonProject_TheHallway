import tkinter

def doButton():

 label_1.configure(text = "Background Story 2")

xd = tkinter.Tk()

label_1 = tkinter.Label(xd, text="Background Story 1")

label_1.pack()

button_1 = tkinter.Button(xd, text="Next", command=doButton)

button_1.pack()

xd.mainloop()
