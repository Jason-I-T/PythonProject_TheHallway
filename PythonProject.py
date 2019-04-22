from tkinter import *


#Functions/Methods
#############################################################
#def go_left():

#def go_right():


#def go_forward():

#def go_back():

#def reset():

#def open_door():

#def talk():

#def read_note():
#############################################################

#Frames
#############################################################
root = Tk()
root.geometry("450x550")
root.configure(bg = "black")


move_butt_frame = Frame(root)
move_butt_frame.pack(side = BOTTOM)

##############################################################


#Creating and placing the 'movement' buttons
left_button = Button(move_butt_frame, text = "<", width = 5, height = 2, bg = "blue", fg = "white")
left_button.grid(row = 0, column = 0) 

right_button = Button(move_butt_frame, text = ">", width = 5, height = 2, bg = "blue", fg = "white")
right_button.grid(row = 0, column = 2)

forward_button = Button(move_butt_frame, text = "^", width = 5, height = 2, bg = "blue", fg = "white")
forward_button.grid(row = 0, column = 1)

backward_button = Button(move_butt_frame, text = "v", width = 5, height = 2, bg = "blue", fg = "white")
backward_button.grid(row = 1, column = 1)

interact_button = Button(move_butt_frame, text = "Interact", width = 5, height = 2, bg = "green", fg = "white") #command = lambda : open_door(), talk(), read_note()
interact_button.grid(row = 1, column = 2)

reset_button = Button(move_butt_frame, text = "RESET", width = 5, height = 2, bg = "red", fg = "white")
reset_button.grid(row = 1, column = 0)







root.mainloop()