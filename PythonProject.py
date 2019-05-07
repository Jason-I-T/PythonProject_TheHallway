from tkinter import *


#Frames
#############################################################
root = Tk()
root.geometry("450x550")
root.title("The Hallway")


move_butt_frame = Frame(root)
move_butt_frame.pack(side = BOTTOM)
##############################################################


#Background
##############################################################
canvas = Canvas(width = 450, height = 550, bg = "black")
canvas.pack()
##############################################################


#Code
############################################################
place_holder = "img0"
img1 = PhotoImage(file = 'Hall1.png')

#############################################################


#Functions/Methods
#############################################################
def transition_background_start(str1 = place_holder):
	if(place_holder == "img0"):
		canvas.create_image(0, 0, image = img1, anchor = NW)
		
		
#############################################################


#Creating and placing the buttons for movement, interaction, and resetting.
left_button = Button(move_butt_frame, text = "<", width = 5, height = 2, bg = "blue", fg = "white")
left_button.grid(row = 0, column = 0) 

right_button = Button(move_butt_frame, text = ">", width = 5, height = 2, bg = "blue", fg = "white")
right_button.grid(row = 0, column = 2)

forward_button = Button(move_butt_frame, text = "^", width = 5, height = 2, bg = "blue", fg = "white")
forward_button.grid(row = 0, column = 1)

backward_button = Button(move_butt_frame, text = "v", width = 5, height = 2, bg = "blue", fg = "white")
backward_button.grid(row = 1, column = 1)

interact_button = Button(move_butt_frame, text = "Interact", width = 5, height = 2, bg = "green", fg = "white", command = transition_background_start)
interact_button.grid(row = 1, column = 2)

reset_button = Button(move_butt_frame, text = "RESET", width = 5, height = 2, bg = "red", fg = "white")
reset_button.grid(row = 1, column = 0)
###############################################################



root.mainloop()