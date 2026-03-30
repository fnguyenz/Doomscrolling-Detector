# this is where the real work is
# detecting objects (like my phone) using the webcam 

# import any modules required
import cv2 as cv # camera process
from ultralytics import YOLO as y # object detection
import time # grace period

# state variables
model = y("yolov8n.pt") # obtain teh only file we need so that we save on storage
phone = 0 # timestamp of when phone was last detected
graceperiod = 5 # this is the time the program waits before stating offtask after seeing phone
vid = cv.VideoCapture(0) # get the webcam

# create a function for detecting, which only activates if user has turned the STUDY timer on
def detect_status():
    global phone

# ret is a boolean to determine if frame is read or not, true if it is read
# frame is the image caught by camera
    ret, frame = vid.read() 

    if not ret:
        return None, "NOCAM" # means no frame captured
    
    # this is the actual detection
    results = model(frame, verbose=False)[0]
    phoneseen = False # no phone in sight as of beginning code

    # loop through to determine what objects are detected
    for box in results.boxes:
        cls = int(box.cls[0]) #cls is class index
        label = model.names[cls] # converts into a label for user to read 

        if label == "cell phone": # cellphone is converted through model.names
            phoneseen = True
    
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

# function to end the camera 
def release():
    vid.release()
    cv.destroyAllWindows()


# # a loop to constantly produce frames and produce video
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