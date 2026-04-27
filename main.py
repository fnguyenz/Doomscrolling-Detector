''' 
DOOM SCROLLING DETECTOR!!!
THIS IS BEING MADE TO CREATE SOME SORT OF ALARM AND DISPLAY WHEN I AM OFF TASK
(OR ON MY PHONE IN SPECIFIC)
MAKE USE OF THE WEBCAM, 
POSSIBLY MAKE A TIMER TO DETERMINE HOW LONG I AM ACTUALLY WORKING VS OFF TASK
'''


# in order to be more organized as this will be long
# i decided to create different python files to section off my code

#import anything required
# includes functions from other files, or modules
import cv2 as cv
from detector import detect_status, release
import ui # importing allows for the gui to play

# create the timer and implement any previously saved settings