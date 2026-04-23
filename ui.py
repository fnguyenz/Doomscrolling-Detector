# this is where the user interface sits
# will use tkinter, pillow, and cv2 to put the webcam into the gui
import tkinter as tk
from PIL import Image, ImageTk # for the image conversion of the webcam!
import cv2 as cv
from detector import vid


# use gui to make this look more organized and easy to navigate
# in this, i will put together all the logic in a pleasing way.
# this also means i manage the timer and detection logic using the tkinter .after() function

# main part
root = tk.Tk()
root.title("Studies")
root.minsize(800,800)
root.config(bg="#DDD8C9")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# colours are #6C4B71 for purple, #F0EEE9 for cream, #DDD8C9 darker cream
#body
bod = tk.Frame(root, bg="#F0EEE9")
bod.grid(padx=30, pady=30, row=0,column=0, sticky="nsew")
bod.grid_propagate(False)

# put items like timer options and webcam inside body
settings = tk.Frame(bod, bg="#F0EEE9")
for i in range(4): 
    bod.grid_columnconfigure(i, weight=1)
    bod.grid_rowconfigure(i,weight=1)
settings.grid(padx=10, pady=10, row=0, column=0,columnspan=4, sticky="news")
settings.grid_propagate(False)

cam = tk.Frame(bod, bg="#F0EEE9")
cam.grid(padx=5,pady=5, row=1,columnspan=2,column=1)


# buttons within settings
subtract = tk.Button(settings, text="-", relief="flat", bg="#F0EEE9", fg="#6C4B71",
                     highlightbackground="#F0EEE9", activebackground="#F0EEE9", 
                     pady=20,padx=30, command=lambda: print("subtract time!"))
subtract.grid(padx=(0,0),pady=(0,0), row=0, column=1, sticky="nsew")

add = tk.Button(settings, text="+",bg="#F0EEE9", relief="flat", fg="#6C4B71", 
                 highlightbackground="#F0EEE9", activebackground="#F0EEE9",
                 pady=20,padx=30, command=lambda: print("add time!"))
add.grid(padx=(0,0),pady=(0,0),row=0,column=4, sticky="nsew")


root.mainloop()