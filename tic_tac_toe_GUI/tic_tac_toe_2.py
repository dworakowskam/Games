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
window_width = 432
window_height = 493
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


# create Button widgets for a play
ipadding = {"ipadx": 12, "ipady": 45}
def return_pressed(event):
    print("Return key pressed.")
    
button1 = ttk.Button(root)
button1.bind('<Button>', return_pressed)
button1.focus()
button1.grid(row=1, column=0, **ipadding, sticky=tk.SE)

button2 = ttk.Button(root)
button2.bind('<Button>', return_pressed)
button2.focus()
button2.grid(row=1, column=1, **ipadding)

button3 = ttk.Button(root)
button3.bind('<Button>', return_pressed)
button3.focus()
button3.grid(row=1, column=2, **ipadding, sticky=tk.W)

button4 = ttk.Button(root)
button4.bind('<Button>', return_pressed)
button4.focus()
button4.grid(row=2, column=0, **ipadding, sticky=tk.E)

button5 = ttk.Button(root)
button5.bind('<Button>', return_pressed)
button5.focus()
button5.grid(row=2, column=1, **ipadding)

button6 = ttk.Button(root)
button6.bind('<Button>', return_pressed)
button6.focus()
button6.grid(row=2, column=2, **ipadding, sticky=tk.W)

button7 = ttk.Button(root)
button7.bind('<Button>', return_pressed)
button7.focus()
button7.grid(row=3, column=0, **ipadding, sticky=tk.NE)

button8 = ttk.Button(root)
button8.bind('<Button>', return_pressed)
button8.focus()
button8.grid(row=3, column=1, **ipadding)

button9 = ttk.Button(root)
button9.bind('<Button>', return_pressed)
button9.focus()
button9.grid(row=3, column=2, **ipadding, sticky=tk.NW)

# # set the disabled flag
# button.state(['disabled'])
# # remove the disabled flag
# button.state(['!disabled'])

photo_x = tk.PhotoImage(file="x.png")
photo_o = tk.PhotoImage(file="o.png")
image_label_example = ttk.Label(
    root,
    image=photo_o,
    padding=5
)
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
