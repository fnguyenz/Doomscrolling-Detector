# this is where the real work is
# detecting objects (like my phone) using the webcam 

# import any modules required
import cv2 as cv # camera process
from ultralytics import YOLO as y # object detection
import time # grace period
from PIL import Image

# state variables
model = y("yolov8n.pt") # obtain the only file we need so that we save on storage
phone = 0 # timestamp of when phone was last detected
graceperiod = 1 # the time the program takes to process whether there is a phone on screen
vid = cv.VideoCapture(0) # get the webcam
width, height = 600, 600 # for the webcam sizes on tkinter
# set the width/height based on these values in order to display at only this size
vid.set(cv.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv.CAP_PROP_FRAME_HEIGHT, height)

# create a function for detecting, which only activates if user has turned the STUDY timer on
def detect_status():
    global phone

# ret is a boolean to determine if frame is read or not, true if it is read
# frame is the image caught by camera
    ret, frame = vid.read() 

    if not ret:
        return None, "NOCAM" # means no frame captured
    
    # for cropping the camera view into a square
    h, w = frame.shape[:2]
    size = min(h, w)

    # make an equation that gets the new x and y to maintain square
    x1 = (w-size)//2 
    y1 = (h-size)//2 #//2 is dividing by 2

    # update the frame according to the new square ratio version
    frame = frame[y1:y1+size, x1:x1+size]
    
    # this is the actual detection
    results = model(frame, verbose=False)[0]
    phoneseen = False # no phone in sight as of beginning code

    # loop through to determine what objects are detected
    for box in results.boxes:
        # ignore any small boxes that app may mistake as phone
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        w = x2 - x1
        h = y2 - y1
        if w*h < 500: # ignore the boxes smaller than 500px
            continue
        cls = int(box.cls[0]) #cls is class index
        con = float(box.conf[0]) # the apps confidence in detection
        label = model.names[cls] # converts into a label for user to read 

        if label == "cell phone" and con > 0.5: # cellphone is converted through model.names
            phoneseen = True
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv.putText(frame, f"{label} {con:.2f}", (x1, y1 - 10),
                    cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)

    
    # phone detection, if becomes true then get the timestamp of when it was seen and if it is still seen
    if phoneseen:
        phone = time.time()
    
    # allow grace period so that it can properly state that user is off task
    # if the time exceeds grace period, set off teh alarm
    if (time.time() - phone) < graceperiod:
        status = "OFFTASK"
    else:
        status = "ONTASK"
    
    return frame, status

# create a function to play a video when off task
def playvid():
    pass
# function to end the camera 
def release():
    vid.release()
    cv.destroyAllWindows()


# used to test and figure out how to work webcam
# a loop to constantly produce frames and produce video
# def cam():
#     global a
#     while True:
#         a=a+1

#         # check is a boolean to check if video is running
#         # frame is the colour values which is being read by the video capturing
#         check, frame = vid.read()
#         cv.imshow("Capturing",frame)

#         # script waits 1 millisecond before taking action
#         key=cv.waitKey(1)

#         # quit the webcam if user presses q
#         if key==ord('q'):
#             break
#     # end the loop and stop running the video once quit
#     vid.release()
#     cv.destroyAllWindows

# cam()