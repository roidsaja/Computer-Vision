import cv2
import numpy as np
import dlib
from imutils import face_utils

# open a camera for video capturing
cap = cv2.VideoCapture(0)

# construct the default face detector
detector = dlib.get_frontal_face_detector()

# an object that helps determine a set of key point locations to define a pose for that object.
predictor = dlib.shape_predictor("/media/thiccpad/Enclosure/shape_predictor_68_face_landmarks.dat")

#status marking for current state
sleep = 0
drowsy = 0
active = 0
status = ""
colour = (0,0,0)

# Hausdorff Distance
def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

def blinked(a,b,c,d,e,f):
    up = compute(b,d) + compute(c,e)
    down = compute(a,f)
    ratio = up / (2.0 * down)

    #Check if it blinks
    if(ratio > 0.3):
        return #none
    elif(ratio > 0.21 and ratio <= 0.3):
        return 1
    else:
        return 0

while True:
    # grabs, decodes and returns the next video frame
    _, frame = cap.read()

    # converts an image from one color space to another
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # detected face in faces array
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1,y1), (x2,y2), (0,255,255), 2)
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # left eye [36:42]
        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        # print("left_blink: ", left_blink)

        # right eye [42:48]
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        # print("right_blink: ", right_blink)

        if(left_blink == 0 or right_blink == 0):
            sleep += 1
            drowsy = 0
            active = 0
            if(sleep > 6):
                status = "ASLEEP!"
                colour = (0,0,255)
        elif(left_blink == 1 or right_blink == 1):
            sleep = 0
            active = 0
            drowsy += 1
            if(drowsy > 6):
                status = "DRIVER IS SLEEPY!"
                colour = (0,255,255)
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if(active > 6):
                status = "AWAKE!"
                colour = (0,255,0)
        
        cv2.putText(frame, status, org=(100,100), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.2, color=colour, thickness=3)

        for n in range(0,68):
            (x,y) = landmarks[n]
            # draws a circle on the landmark points
            cv2.circle(face_frame, center=(x,y), radius=2, color=(255,255,255), thickness=-1)
        
        cv2.imshow("Result", frame)
        cv2.imshow("Landmarks", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break