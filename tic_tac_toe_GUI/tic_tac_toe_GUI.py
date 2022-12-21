# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:21:56 2022

@author: MD
"""

import tkinter as tk # import the old Tk themed widgets
from tkinter import ttk # import the new Tk themed widgets
from ctypes import windll 
windll.shcore.SetProcessDpiAwareness(1) # fix blurry text and UI



class MainFrame(ttk.Frame):
    """ Creates frame with an entry
    """
    
    def __init__(self, game):
        super().__init__(game)
        self.__create_widgets()
        
    def __create_widgets(self):
        """ Creates widgets on entry frame """
        self.instruction = "You have to put three of your marks\nin a horizontal, vertical,\n\
        or diagonal row to win.\nClick in the space\nyou want to place your piece."
        self.instruction=ttk.Label( # place a label with game instruction on the root window
            text=self.instruction,
            background="cornsilk2",
            relief="solid",
            justify=tk.CENTER,
            padding=32,
            font=("Verdana", 10))
        self.instruction.grid(row=0, ipady=75) 
        self.play_button = ttk.Button(text="PLAY")# create button widget for starting a game
        self.play_button.grid(row=1, pady=40, ipady=20)
        self.play_button.bind('<Button>', self.change_frame) # bind play button with a function
    
    def return_pressed(self, frame):
        """ Puts X or O mark in a clicked space """
        self.mark = ttk.Label(frame, text = " X", font=("Verdana", 45))
        self.mark.grid(row=0, column=0, ipadx=17)    
    
    
    def change_frame(self, event):
        """ Handles PLAY button click event and creates new widgets for play """
        self.instruction.grid_forget() # erases entry label
        self.play_button.grid_forget() # erases PLAY button
        self.message = "  Click on the square to put your mark"
        self.message = ttk.Label( # place a label on the root window
            text=self.message,
            background="cornsilk2",
            relief="solid",
            padding=9,
            font=("Verdana", 10))
        self.message.grid(row=0, columnspan=3, ipadx=17, ipady=35)
        self.frame1 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame1.grid(row=1, column=0, sticky=tk.SE) 
        self.button1 = ttk.Button(self.frame1, command=lambda:self.return_pressed(self.frame1))
        self.button1.grid(ipadx=12, ipady=45)
        self.frame2 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame2.grid(row=1, column=1)  
        self.button2 = ttk.Button(self.frame2, command=lambda:self.return_pressed(self.frame2))
        self.button2.grid(ipadx=12, ipady=45)
    
            
    
class TicTacToe(tk.Tk):
    """ Creates a root window
    """
    
    def __init__(self):
        super().__init__()
        self.window_width = 437 # determine window width
        self.window_height = 497 # determine window height
        self.title("TIC TAC TOE") # set the title
        self.iconbitmap("favicon.ico") # set default icon
        self.resizable(False, False) # set resizable variable as false for both width and height
        self.screen_width = self.winfo_screenwidth() # get the width of a window 
        self.screen_height = self.winfo_screenheight() # get the height of a window
        self.center_x = int(self.winfo_screenwidth()/2 - self.window_width/2) # set x value for centering window
        self.center_y = int(self.winfo_screenheight()/2 - self.window_height/2) # set y value for centering window
        self.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}") # set window size and position
        

        
    
if __name__ == "__main__":
    
    entry = TicTacToe()
    main_frame = MainFrame(entry)
    entry.mainloop() # keep the window displaying
