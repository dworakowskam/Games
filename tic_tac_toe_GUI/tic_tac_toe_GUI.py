# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:21:56 2022

@author: MD
"""

# import the old Tk themed widgets
import tkinter as tk
# import the new Tk themed widgets
from tkinter import ttk
# fix blurry text and UI
from ctypes import windll 
windll.shcore.SetProcessDpiAwareness(1)


class TicTacToe(tk.Tk):
    window_width = 437 # determine window width
    window_height = 497 # determine window height
    
    # Handles an instance of a Tic Tac Toe game
    def __init__(self):
        super().__init__()
        self.title("TIC TAC TOE") # set the title
        self.iconbitmap("favicon.ico") # set default icon
        self.resizable(False, False) # set resizable variable as false for both width and height
        self.screen_width = self.winfo_screenwidth() # get the width of a window 
        self.screen_height = self.winfo_screenheight() # get the height of a window
        self.center_x = int(self.winfo_screenwidth()/2 - self.window_width/2) # set x value for centering window
        self.center_y = int(self.winfo_screenheight()/2 - self.window_height/2) # set y value for centering window
        self.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}") # set window size and position
        
    
if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop() # keep the window displaying
    
    

