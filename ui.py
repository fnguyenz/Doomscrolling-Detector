# this is where the user interface sits
# will use tkinter, pillow, and cv2 to put the webcam into the gui
import tkinter as tk
from PIL import Image, ImageTk # for the image conversion of the webcam!
import cv2 as cv
from detector import detect_status


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
settings.grid_rowconfigure(0, weight=1)
settings.grid(padx=10, row=0, column=0,columnspan=4, sticky="news")
settings.grid_propagate(False)

for i in range(4): 
    bod.grid_columnconfigure(i, weight=1)
    bod.grid_rowconfigure(i,weight=1)
    settings.grid_columnconfigure(i, weight=1)

# for the webcam to appear on the gui
camlabel = tk.Label(bod, bg="#FFFFFF")
camlabel.grid(row=2,column=1, columnspan=2)

statuslabel = tk.Label(bod, bg="#F0EEE9")
statuslabel.grid(row=3, column=2, sticky="nsw")

# buttons within settings
subtract = tk.Button(settings, text="-", relief="flat", bg="#F0EEE9", fg="#6C4B71",
                    highlightbackground="#F0EEE9", activebackground="#F0EEE9", 
                    pady=20,padx=30, command=lambda: print("subtract time!"))
subtract.grid(padx=(0,0),pady=(0,0), row=0, column=0, sticky="nse")

add = tk.Button(settings, text="+",bg="#F0EEE9", relief="flat", fg="#6C4B71", 
                highlightbackground="#F0EEE9", activebackground="#F0EEE9",
                pady=20,padx=30, command=lambda: print("add time!"))
add.grid(padx=(0,0),pady=(0,0),row=0,column=3, sticky="nsw")

# timer length
timer = tk.Label(settings, text="0:00", bg="#FFFFFF", fg="#DDD8C9", font=("Dynapuff", 40))
timer.grid(padx=10, pady=5, row=0, column=1, columnspan=2, sticky="new")

# start timer button / later transforms to pause if already started
timerbutton = tk.Button(bod, text="start", relief="flat",bg="#F0EEE9", fg="#6C4B71",
                        highlightbackground="#F0EEE9", activebackground="#F0EEE9",
                        pady=20,padx=30,command=lambda: print("timer started!"))
timerbutton.grid(padx=(0,0),pady=(0,0), row=1, column=1, columnspan=2, sticky="sew")

# function for continuously displaying and updating the camera
def updatecam():
    global lasttk
    frame, status = detect_status()
    # if there is no frame, dont update, if there is, make proper update protocols
    if frame is not None:
        # when condition doesnt apply, blur out the image
        # play video/display a message and blare a noise to alarm the user to get working!
        if status == "OFFTASK":
                frame = cv.GaussianBlur(frame, (25,25), 0)

        # otherwise, convert opencv frames from bgr to rgb
        # replace old frame with rbg frames to get the current frame
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # convert to pil image to heelp convert to a more compatible file for tkinter
        img = Image.fromarray(frame)        

        # convert to tkinter friendly file
        imgtk = ImageTk.PhotoImage(image=img)        
        #updating the camera label
        #this turns camlabel.imgtk into the tkinter image file we made above
        camlabel.imgtk = imgtk
        camlabel.configure(image=imgtk)


        # if user is ontask, state that on the screen and allow frames to continue
        if status == "ONTASK":
            statuslabel.config(text="On Task", fg="#4B7155", font=("Dynapuff", 20)) # stating that the user is still ontask
        else:
            statuslabel.config(text="Off Task", fg="#714B4E", font=("Dynapuff", 20)) # user is off task if the condition doesnt apply!

    # continuously call this after specific time
    camlabel.after(5, updatecam)

#ensure the camera gets updated
updatecam()
# run the ui itself!
root.mainloop()