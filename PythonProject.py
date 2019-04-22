from tkinter import *


#Functions/Methods
#############################################################
#def go_left():

#def go_right():


#def go_forward():

#def go_back():


#############################################################

#Frames
#############################################################
root = Tk()
root.geometry("450x550")
root.configure(bg = "black")


move_butt_frame = Frame(root, bg = "black")
move_butt_frame.pack(side = BOTTOM)

##############################################################


#Creating and placing the 'movement' buttons
left_button = Button(move_butt_frame, text = "<", width = 5, height = 2, bg = "blue", fg = "white")
left_button.grid(row = 0, column = 0, rowspan = 2) 

right_button = Button(move_butt_frame, text = ">", width = 5, height = 2, bg = "blue", fg = "white")
right_button.grid(row = 0, column = 2, rowspan = 2)

forward_button = Button(move_butt_frame, text = "^", width = 5, height = 2, bg = "blue", fg = "white")
forward_button.grid(row = 0, column = 1)

backward_button = Button(move_butt_frame, text = "v", width = 5, height = 2, bg = "blue", fg = "white")
backward_button.grid(row = 1, column = 1)









root.mainloop()