import tkinter as tk # import the old Tk themed widgets
from tkinter import ttk # import the new Tk themed widgets
from ctypes import windll 
windll.shcore.SetProcessDpiAwareness(1) # fix blurry text and UI



class MainFrame(ttk.Frame):
    
    instruction = "You have to put three of your marks\nin a horizontal, vertical,\n\
    or diagonal row to win.\nClick in the space\nyou want to place your piece."
    
    def __init__(self, game):
        super().__init__(game)
        self.__create_widgets()
        
    def __create_widgets(self):
        self.instruction=ttk.Label( # place a label with game instruction on the root window
            text=self.instruction,
            background="cornsilk2",
            relief="solid",
            justify=tk.CENTER,
            padding=32,
            font=("Verdana", 10),
            )
        self.instruction.grid(row=0, ipady=75) # place instruction on the grid
        self.play_button = ttk.Button(text="PLAY")# create button widget for starting a game
        self.play_button.grid(row=1, pady=40, ipady=20) # place play button on the grid
        #self.play_button.bind('<Button>', pressed_play) # bind play button with a function
 
    
class TicTacToe(tk.Tk):
    
    window_width = 437 # determine window width
    window_height = 497 # determine window height
    
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
        
    def pressed_play(self):
    #
        pass
        
    
    
if __name__ == "__main__":
    
    game = TicTacToe()
    frame = MainFrame(game)
    game.mainloop() # keep the window displaying
    
    

