import numpy as np
import cv2

face_cascade_name = "./harr/haarcascade_frontalface_alt.xml"
eyes_cascade_name = "./harr/haarcascade_eye.xml"



def detectAndDisplay(frame) :
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray)

    for (x,y,w,h) in faces :
#       center = (x + w//2 , y + h //2 )
        frame = cv2.rectangle(frame, (x,y) , (x+w,y+h),(0,0,255),4)
        faceGOT = frame_gray[y:y+h,x:x+w]
        eyes  = eyes_cascade.detectMultiScale(faceGOT)
        for (x2,y2,w2,h2) in eyes :
            eye_center = (x + x2 + w2//2 , y + y2 + h2//2)
            radius = int(round((w2+h2)*0.25))
            frame = cv2.circle(frame, eye_center,radius,(0,255,0),4)
    cv2.imshow('HAAR face',frame)


face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

#cascade 따오기
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print("no file  x ")
    exit(0)

if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print("no file x ")
    exit(0)

cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print("no video")
while True:
    ret, frame = cap.read()
    if frame is None:
        print("no captured frame _ out")
        break
    detectAndDisplay(frame)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break;

cv2.waitKey(0)
cv2.destroyAllWindows()