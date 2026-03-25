''' 
DOOM SCROLLING DETECTOR!!!
THIS IS BEING MADE TO CREATE SOME SORT OF ALARM AND DISPLAY WHEN I AM OFF TASK
(OR ON MY PHONE IN SPECIFIC)
MAKE USE OF THE WEBCAM, 
POSSIBLY MAKE A TIMER TO DETERMINE HOW LONG I AM ACTUALLY WORKING VS OFF TASK
'''
# import any modules required
import cv2 as cv, tkinter as tk, time # this will be used to access the webcam, to create a gui, and help create a timer after set amount of time
from PIL import Image # used to create an alarm
from ultralytics import YOLO as yolo

# state variables
model = yolo("/path/to/local/yolov8n.pt") # obtain teh only file we need so that we save on storage
phone = None


####### COME BACK TO THIS LATER<<<<modules are not importing or installing as meant to be





# objects (just for easier management and separation)
# vid = cv2.VideoCapture(0)


# # create functions for detecting, activating, and anything else needed while making this
# #this is the actual logic behind the doomscrolling, using the camera and some sort of imaging to help depict what to look for
# def detection():
#     pass

# # this will be the gui button to call for any doomscrolling found by the user
# def start():
#     detection()

# def wtvfunction():
#     pass


# # use gui to make this look more organized and easy to navigate
# root = tk.Tk()
# root.title("Studies")
# root.minsize(900,900)
# root.config(bg="#BE9D71")

# root.mainloop()
