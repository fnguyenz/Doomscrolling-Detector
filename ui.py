# this is where the user interface sits
# will use tkinter, pillow, and cv2 to put the webcam into the gui
import tkinter as tk
from PIL import Image, ImageTk # for the image conversion of the webcam!
import cv2 as cv
from detector import detect_status

# variables for the timer
running = False
totalseconds = 0 # at default, there is nothing in the timer

# functions for adding and removing time
# these functions need to be above to ensure that the gui knows what the functions are



def subtract():
    global totalseconds

    #remove 60 seconds (a minute)
    if totalseconds >= 60: # restrict it to ensure that time doesnt go into negatives
        totalseconds -= 60
    else:
        totalseconds = 0
    refresh()

def add():
    global totalseconds
    # add 60 seconds (a minute)

    totalseconds +=60
    refresh()

# use gui to make this look more organized and easy to navigate
# in this, i will put together all the logic in a pleasing way.
# this also means i manage the timer and detection logic using the tkinter .after() function
# main part
root = tk.Tk()
root.title("Studies")
root.minsize(800,800)
root.config(bg="#C9DDCB")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# colours are #6C4B71 for purple, #F0EEE9 for cream, #DDD8C9 darker cream
#body
bod = tk.Frame(root, bg="#E9F0E9")
bod.grid(padx=30, pady=30, row=0,column=0, sticky="nsew")
bod.grid_propagate(False)

# put items like timer options and webcam inside body
settings = tk.Frame(bod, bg="#E9F0E9")
settings.grid_rowconfigure(0, weight=1)
settings.grid(padx=10, row=0, column=0,columnspan=4, sticky="news")
settings.grid_propagate(False)

for i in range(4): 
    bod.grid_columnconfigure(i, weight=1)
    settings.grid_columnconfigure(i, weight=1)
    bod.grid_rowconfigure(0,weight=1)

# for the webcam to appear on the gui
camlabel = tk.Label(bod, bg="#FFFFFF")
camlabel.grid(row=2,column=1, columnspan=2)

statuslabel = tk.Label(bod, bg="#E9F0E9")
statuslabel.grid(row=3, column=2, sticky="nsw")

# buttons within settings

subtract = tk.Button(settings, text="-", relief="flat", bg="#E9F0E9", fg="#52714B",
                    highlightbackground="#E9F0E9", activebackground="#E9F0E9", 
                    pady=20,padx=30, command=subtract)
subtract.grid(padx=(0,0),pady=(0,0), row=0, column=0, sticky="nse")

add = tk.Button(settings, text="+",bg="#E9F0E9", relief="flat", fg="#52714B", 
                highlightbackground="#E9F0E9", activebackground="#E9F0E9",
                pady=20,padx=30, command=add)
add.grid(padx=(0,0),pady=(0,0),row=0,column=3, sticky="nsw")

# timer length
timer = tk.Label(settings, text="00:00", bg="#FFFFFF", fg="#C9DDCB", font=("Dynapuff", 40))
timer.grid(padx=10, pady=5, row=0, column=1, columnspan=2, sticky="nesw")

# start timer button / later transforms to pause if already started
timerbutton = tk.Button(bod, text="start", relief="flat",bg="#E9F0E9", fg="#52714B",
                        highlightbackground="#E9F0E9", activebackground="#E9F0E9",
                        pady=20,padx=30, font=("Dynapuff", 20),command=lambda: print("timer started!"))
timerbutton.grid(padx=(0,0),pady=(0,0), row=1, column=1, columnspan=2, sticky="sew")


#refresh the timer
def refresh():
    hours = (totalseconds // 3600) % 24
    mins = (totalseconds % 3600) // 60 # for rounding to the nearest integer
    secs = totalseconds % 60 # for keeping it counting up to 60 max

    # edit the timer label to ensure that itll refresh!
    if hours > 0:
        timer.config(text=f"{hours:02}:{mins:02}:{secs:02}") # display hours once mins reaches 60
    else:
        timer.config(text=f"{mins:02}:{secs:02}") # {variable:digit} displays the numbers by 2 digits only

# function for continuously displaying and updating the camera
def updatecam():
    global lasttk
    global running
    frame, status = detect_status()
    # if there is no frame, dont update, if there is, make proper update protocols
    if frame is not None:
        # when condition doesnt apply, blur out the image
        # play video/display a message and blare a noise to alarm the user to get working!
        if status == "OFFTASK":
                statuslabel.config(text="Off Task", fg="#714B4E", font=("Dynapuff", 20))
                frame = cv.GaussianBlur(frame, (25,25), 0)
                running = False
        else:
        # user is on task if the condition doesnt apply!  
        # if user is ontask, state that on the screen and allow frames to continue
            running = True
            statuslabel.config(text="On Task", fg="#4B7155", font=("Dynapuff", 20)) # stating that the user is still ontask

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



    # continuously call this after specific time
    camlabel.after(10, updatecam)

#ensure the camera gets updated
# studytime()
updatecam()
# run the ui itself!
root.mainloop()