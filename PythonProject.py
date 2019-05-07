from tkinter import *
from tkinter import messagebox

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

x = messagebox.showinfo("Instruction", "Press interact to start.")
##############################################################


#Image/Place_holder Storage
############################################################
img1 = PhotoImage(file = 'Hall1.png')
img2 = PhotoImage(file = 'Hall2.png')
img3 = PhotoImage(file = 'Hall3.png')
img4 = PhotoImage(file = 'Hallway4.png')
place_holder = 0


#############################################################


#Functions/Methods
#############################################################
def change_bg_start():	
	global place_holder
	if(place_holder == 0):
		canvas.create_image(0, 0, image = img1, anchor = NW)
		place_holder = 1

def change_bg_fwd():
	global place_holder
	if(place_holder == 1):
		canvas.delete("all")
		canvas.create_image(0, 0, image = img4, anchor = NW)
		place_holder = 2

def change_bg_lft():
	global place_holder
	if(place_holder == 2):
		canvas.delete("all")
		canvas.create_image(0, 0, image = img2, anchor = NW)
		place_holder = 6

def change_bg_right():
	global place_holder
	if(place_holder == 2):
		canvas.delete("all")
		canvas.create_image(0, 0, image = img3, anchor = NW)
		place_holder = 5
		messagebox.showinfo("Instruction", "You have escaped from the building.")


def change_bg_back():
	global place_holder


	if(place_holder == 5):
		canvas.delete("all")
		canvas.create_image(0, 0, image = img4, anchor = NW)
		place_holder = 2

	if(place_holder == 6):
		canvas.delete("all")
		canvas.create_image(0, 0, image = img4, anchor = NW)
		place_holder = 2

	if(place_holder == 2):
		canvas.delete("all")
		canvas.create_image(0, 0, image = img1, anchor = NW)
		place_holder = 1


def reset_ohnoes():
	global place_holder
	canvas.delete("all")
	place_holder = 0

#############################################################


#Creating and placing the buttons for movement, interaction, and resetting.
left_button = Button(move_butt_frame, text = "<", width = 5, height = 2, bg = "blue", fg = "white", command = change_bg_lft)
left_button.grid(row = 0, column = 0) 

right_button = Button(move_butt_frame, text = ">", width = 5, height = 2, bg = "blue", fg = "white", command = change_bg_right)
right_button.grid(row = 0, column = 2)

forward_button = Button(move_butt_frame, text = "^", width = 5, height = 2, bg = "blue", fg = "white", command = change_bg_fwd)
forward_button.grid(row = 0, column = 1)

backward_button = Button(move_butt_frame, text = "v", width = 5, height = 2, bg = "blue", fg = "white", command = change_bg_back)
backward_button.grid(row = 1, column = 1)

interact_button = Button(move_butt_frame, text = "Interact", width = 5, height = 2, bg = "green", fg = "white", command = change_bg_start)
interact_button.grid(row = 1, column = 2)

reset_button = Button(move_butt_frame, text = "RESET", width = 5, height = 2, bg = "red", fg = "white", command = reset_ohnoes)
reset_button.grid(row = 1, column = 0)
###############################################################



root.mainloop()