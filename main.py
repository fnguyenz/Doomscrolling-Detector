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

# create the timer itself

# create loop to connect everything togehter
while True:
    frame, status = detect_status()
    # if no frame then cancel
    if frame is None:
        break

    cv.putText(frame,status, (20,40),
               cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    
    # this is the image of the user being projected
    cv.imshow("Detector", frame)

    # quit camera overall
    if cv.waitKey(1) == 27: # the escape key
        break
release()