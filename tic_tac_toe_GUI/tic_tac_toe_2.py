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
window_width = 437
window_height = 497
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# place a label on the root window
message = " Click on the square to put your mark"
message = ttk.Label(
    root,
    text=message,
    background="cornsilk2",
    relief="solid",
    padding=9,
    font=("Verdana", 10)
    )
message.grid(row=0, columnspan=3, ipadx=15, ipady=35)


# create Button widgets and frames for play
ipadding = {"ipadx": 12, "ipady": 45}
def return_pressed(event):
    print("Return key pressed.")
    
frame1 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame1.grid(row=1, column=0, sticky=tk.SE)    
button1 = ttk.Button(frame1)
button1.bind('<Button>', return_pressed)
button1.grid(**ipadding)

frame2 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame2.grid(row=1, column=1)  
button2 = ttk.Button(frame2)
button2.bind('<Button>', return_pressed)
button2.grid(**ipadding)

frame3 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame3.grid(row=1, column=2, sticky=tk.W)  
button3 = ttk.Button(frame3)
button3.bind('<Button>', return_pressed)
button3.grid(**ipadding)

frame4 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame4.grid(row=2, column=0, sticky=tk.E) 
button4 = ttk.Button(frame4)
button4.bind('<Button>', return_pressed)
button4.grid(**ipadding)

frame5 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame5.grid(row=2, column=1) 
button5 = ttk.Button(frame5)
button5.bind('<Button>', return_pressed)
button5.grid(**ipadding)

frame6 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame6.grid(row=2, column=2, sticky=tk.W) 
button6 = ttk.Button(frame6)
button6.bind('<Button>', return_pressed)
button6.grid(**ipadding)

frame7 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame7.grid(row=3, column=0, sticky=tk.NE) 
button7 = ttk.Button(frame7)
button7.bind('<Button>', return_pressed)
button7.grid(**ipadding)

frame8 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame8.grid(row=3, column=1, sticky=tk.NE) 
button8 = ttk.Button(frame8)
button8.bind('<Button>', return_pressed)
button8.grid(**ipadding)

frame9 = ttk.Frame(root, borderwidth=1, relief="ridge")
frame9.grid(row=3, column=2, sticky=tk.NW) 
button9 = ttk.Button(frame9)
button9.bind('<Button>', return_pressed)
button9.grid(**ipadding)

# # # set the disabled flag
# # button.state(['disabled'])
# # # remove the disabled flag
# # button.state(['!disabled'])

# photo_x = tk.PhotoImage(file="x.png")
# photo_o = tk.PhotoImage(file="o.png")
# image_label_example = ttk.Label(
#     frame,
#     image=photo_o,
#     padding=5
# )
#image_label_example.pack(side=tk.LEFT)


# # exit button PROGRAM SIĘ WIESZA!!!
# exit_button = ttk.Button(
#     root,
#     text='Exit',
#     command=lambda: root.quit() # program się wiesza
# )

# exit_button.pack(
#     ipadx=5,
#     ipady=5,
#     expand=True
# )

# keep the window displaying
root.mainloop()
