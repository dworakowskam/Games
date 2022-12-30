# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:21:56 2022

@author: MD
"""

import tkinter as tk # import the old Tk themed widgets
from tkinter import ttk # import the new Tk themed widgets
from ctypes import windll 
windll.shcore.SetProcessDpiAwareness(1) # fix blurry text and UI
import random



class MainFrame(ttk.Frame):
    """ Creates frame with an entry """
    
    def __init__(self, game):
        super().__init__(game)
        self.create_entry_widgets()
        self.empty_spaces = []
        self.again = 0
        
    def create_entry_widgets(self):
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
        self.play_button = ttk.Button(text="PLAY") # creates button widget for starting a game
        self.play_button.grid(row=1, pady=40, ipady=20)
        self.play_button.bind('<Button>', self.change_frame) # binds play button with a function
    
    def change_frame(self, event):
        """ Handles PLAY button click event and creates new widgets for play """
        self.instruction.grid_forget() # erases entry label
        self.play_button.grid_forget() # erases PLAY button
        if self.again == 1:
            self.result.grid_forget()
            self.empty_spaces = []
        self.message = "  Click on the square to put your mark"
        self.message = ttk.Label( # place a label on the root window
            text=self.message,
            background="cornsilk2",
            relief="solid",
            padding=9,
            font=("Verdana", 10))
        self.message.grid(row=0, columnspan=3, ipadx=17, ipady=35)
        
        # create frames to be clicked to put a mark:
        self.frame1 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame1.grid(row=1, column=0, sticky=tk.SE)
        self.empty_spaces.append(self.frame1) # appends a frame to the list of yet not clicked spaces
        self.button1 = ttk.Button(self.frame1, command=lambda:self.return_pressed(self.frame1)) # creates button in a frame
        self.button1.grid(ipadx=12, ipady=45)
        
        self.frame2 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame2.grid(row=1, column=1)  
        self.empty_spaces.append(self.frame2)
        self.button2 = ttk.Button(self.frame2, command=lambda:self.return_pressed(self.frame2))
        self.button2.grid(ipadx=12, ipady=45, sticky=tk.S)
        
        self.frame3 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame3.grid(row=1, column=2, sticky=tk.SW)  
        self.empty_spaces.append(self.frame3)
        self.button3 = ttk.Button(self.frame3, command=lambda:self.return_pressed(self.frame3))
        self.button3.grid(ipadx=12, ipady=45)
        
        self.frame4 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame4.grid(row=2, column=0, sticky=tk.E)  
        self.empty_spaces.append(self.frame4)
        self.button4 = ttk.Button(self.frame4, command=lambda:self.return_pressed(self.frame4))
        self.button4.grid(ipadx=12, ipady=45, sticky=tk.E)
        
        self.frame5 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame5.grid(row=2, column=1)  
        self.empty_spaces.append(self.frame5)
        self.button5 = ttk.Button(self.frame5, command=lambda:self.return_pressed(self.frame5))
        self.button5.grid(ipadx=12, ipady=45)
        
        self.frame6 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame6.grid(row=2, column=2, sticky=tk.W)  
        self.empty_spaces.append(self.frame6)
        self.button6 = ttk.Button(self.frame6, command=lambda:self.return_pressed(self.frame6))
        self.button6.grid(ipadx=12, ipady=45, sticky=tk.W)
        
        self.frame7 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame7.grid(row=3, column=0, sticky=tk.NE) 
        self.empty_spaces.append(self.frame7)
        self.button7 = ttk.Button(self.frame7, command=lambda:self.return_pressed(self.frame7))
        self.button7.grid(ipadx=12, ipady=45, sticky=tk.NE)
        
        self.frame8 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame8.grid(row=3, column=1)  
        self.empty_spaces.append(self.frame8)
        self.button8 = ttk.Button(self.frame8, command=lambda:self.return_pressed(self.frame8))
        self.button8.grid(ipadx=12, ipady=45, sticky=tk.N)
        
        self.frame9 = ttk.Frame(borderwidth=1, relief="ridge")
        self.frame9.grid(row=3, column=2, sticky=tk.NE)  
        self.empty_spaces.append(self.frame9)
        self.button9 = ttk.Button(self.frame9, command=lambda:self.return_pressed(self.frame9))
        self.button9.grid(ipadx=12, ipady=45, sticky=tk.NW)
    
    def return_pressed(self, frame):
        """ Puts X mark in a clicked space """
        self.mark = ttk.Label(frame, text = " X", font=("Verdana", 45)) # creates an X label in the clicked frame
        self.mark.grid(row=0, column=0, ipadx=17)    
        self.set_frame_state_as_x(frame)
        if self.check_winner() == True:
            self.print_end_result("X")
            self.disable_unclicked_buttons()
        else:
            self.empty_spaces.remove(frame)
            self.put_mark_in_random_space(frame)
        
    def set_frame_state_as_x(self, frame):
        """ Sets the value of a frame as "X" """
        if frame == self.frame1:
            self.frame1 = "X"
        elif frame == self.frame2:
            self.frame2 = "X"
        elif frame == self.frame3:
            self.frame3 = "X"
        elif frame == self.frame4:
            self.frame4 = "X"
        elif frame == self.frame5:
            self.frame5 = "X"
        elif frame == self.frame6:
            self.frame6 = "X"
        elif frame == self.frame7:
            self.frame7 = "X"
        elif frame == self.frame8:
            self.frame8 = "X"
        elif frame == self.frame9:
            self.frame9 = "X"
            
    def check_winner(self):
        """ Checks if there are three same marks in a row, column or diagonal """
        if self.frame1 == self.frame2 == self.frame3 or\
            self.frame4 == self.frame5 == self.frame6 or\
                self.frame7 ==self.frame8 == self.frame9: # checks rows
                    return True
        if self.frame1 == self.frame4 == self.frame7 or\
            self.frame2 == self.frame5 == self.frame8 or\
                self.frame3 ==self.frame6 == self.frame9: # checks columns
                    return True
        if self.frame1 == self.frame5 == self.frame9 or\
            self.frame3 == self.frame5 == self.frame7: # checks diagonals
                return True
        return False
                    
    def put_mark_in_random_space(self, frame):
        """ Puts O mark in a random space """
        if len(self.empty_spaces) > 0:  # checks if there are any empty spaces left
            self.random_space = random.choice(self.empty_spaces) # randomly choses a space to put "O" mark
            self.mark = ttk.Label(self.random_space, text = " O", font=("Verdana", 45)) # creates an X label in the randomly chosen frame
            self.mark.grid(row=0, column=0, ipadx=17)
            self.empty_spaces.remove(self.random_space)
            self.set_frame_state_as_o()
            if self.check_winner() == True:
                self.print_end_result("O")
                self.disable_unclicked_buttons()
        else:
            self.print_end_result("draw")
            self.disable_unclicked_buttons()
        
    def set_frame_state_as_o(self):
        """ Sets the value of a frame as "X" """
        if self.random_space == self.frame1:
            self.frame1 = "O"
        elif self.random_space == self.frame2:
            self.frame2 = "O"
        elif self.random_space == self.frame3:
            self.frame3 = "O"
        elif self.random_space == self.frame4:
            self.frame4 = "O"
        elif self.random_space == self.frame5:
            self.frame5 = "O"
        elif self.random_space == self.frame6:
            self.frame6 = "O"
        elif self.random_space == self.frame7:
            self.frame7 = "O"
        elif self.random_space == self.frame8:
            self.frame8 = "O"
        elif self.random_space == self.frame9:
            self.frame9 = "O"
        
    def print_end_result(self, result):
        """ Prints end result  """
        if result == "draw":
            text = "IT'S A DRAW"
            background = "wheat3"
        elif result == "O":
            text = "O WINS"
            background = "red"
        elif result == "X":
            text = "X WINS"
            background = "olive drab4"
        self.result=ttk.Label( 
            text=text,
            background=background,
            relief="solid",
            padding=9,
            justify=tk.CENTER,
            font=("Verdana", 20))    
        self.result.grid(row=0, columnspan=3, rowspan=2)
        self.decide_what_next()
        
    def disable_unclicked_buttons(self):
        """ Sets the state of unclicked space buttons as disabled when game is over """
        if self.frame1 != "X" or "O":
            self.button1.config(state="disabled")
        if self.frame2 != "X" or "O":
            self.button2.config(state="disabled")
        if self.frame3 != "X" or "O":
            self.button3.config(state="disabled")
        if self.frame4 != "X" or "O":
            self.button4.config(state="disabled")
        if self.frame5 != "X" or "O":
            self.button5.config(state="disabled")
        if self.frame6 != "X" or "O":
            self.button6.config(state="disabled")
        if self.frame7 != "X" or "O":
            self.button7.config(state="disabled")
        if self.frame8 != "X" or "O":
            self.button8.config(state="disabled")
        if self.frame9 != "X" or "O":
            self.button9.config(state="disabled")
        
    def decide_what_next(self):
        """ Asks player if he wants to play again or quit  """
        self.play_again = ttk.Button(text="PLAY AGAIN")
            # background="cornsilk2",
            # relief="solid",
            # padding=15,
            # justify=tk.CENTER,
            # font=("Verdana", 10))
        self.play_again.grid(row=3, column=0)
        self.again = 1
        self.play_again.bind('<Button>', self.change_frame)
        self.quit = ttk.Button(text="QUIT", command=self.quit_game)
            # background="cornsilk2",
            # relief="solid",
            # padding=15,
            # justify=tk.CENTER,
            # font=("Verdana", 10))
        self.quit.grid(row=3, column=2)
        
    def quit_game(self):
        entry.destroy()
    
class TicTacToe(tk.Tk):
    """ Creates a root window """
    
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
