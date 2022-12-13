# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:21:34 2022

@author: MD
"""
# START DISPLAYING AN IMAGE
# import the classic Tk themed widgets
import tkinter as tk
# import the new Tk themed widgets
from tkinter import ttk

# fix blurry text and UI
from ctypes import windll 
windll.shcore.SetProcessDpiAwareness(1)
    


# create an instance of the tk.Tk class that will create the application window
root = tk.Tk()
root.resizable(False, False) # neither width and height of the window can be resizable

# title the root window and set default icon
root.title("TIC TAC TOE")
root.iconbitmap("favicon.ico")


# determine window size and center the window on the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# place a label on the root window
instruction = "You have to put three of your marks \nin a horizontal, vertical, \
or diagonal row to win. \n Please enter your coordinates in format row,col, \nwhere \
row is the row number \nand col is the column number you want to place your piece."
message = ttk.Label(
    root,
    text =instruction,
    background="cornsilk2",
    relief="solid",
    justify=tk.CENTER,
    padding=10,
    font=("Verdana", 9))
message.pack()


# create Button widget for a play
def return_pressed(event):
    print("Return key pressed.")
button = ttk.Button(root, text="PLAY")
button.bind('<Button>', return_pressed)
button.focus()
button.pack()


# keep the window displaying
root.mainloop()