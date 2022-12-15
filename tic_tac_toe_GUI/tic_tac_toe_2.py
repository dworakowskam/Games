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
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# place a label on the root window
message = "Click on the square to put your mark"
message = ttk.Label(
    root,
    text=message,
    background="cornsilk2",
    relief="solid",
    justify=tk.CENTER,
    padding=20,
    font=("Verdana", 9)
)
message.pack()


# create Button widgets for a play
ipadding = {"ipadx": 5, "ipady": 40}
def return_pressed(event):
    print("Return key pressed.")
photo_x = tk.PhotoImage(file="x.png")
button1 = ttk.Button(root)
button1.bind('<Button>', return_pressed)
button1.focus()
button1.pack(side=tk.LEFT, expand=True, **ipadding)
button2 = ttk.Button(root)
button2.bind('<Button>', return_pressed)
button2.focus()
button2.pack(side=tk.LEFT, expand=True, **ipadding)
button3 = ttk.Button(root)
button3.bind('<Button>', return_pressed)
button3.focus()
button3.pack(side=tk.LEFT, expand=True, **ipadding)


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
