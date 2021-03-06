import numpy as np
import cv2

def detectAndDisplay(frame) :
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray)

    for (x,y,w,h) in faces :
        center = (x + w//2 , y + h //2 )
        frame = cv2.rectangle(frame, (x,y) , (x+w,y+h),(0,0,255),4)
        faceGOT = frame_gray[y:y+h,x:x+w]
        eyes  = eyes_cascade.detectMultiScale(faceGOT)
        for (x2,y2,w2,h2) in eyes :
            eye_center = (x + x2 + w2//2 , y + y2 + h2//2)
            radius = int(round((w2+h2)*0.25))
            frame = cv2.circle(frame, eye_center,radius,(0,255,0),4)
        cv2.imshow('HAAR face',frame)


img =  cv2.imread("./image/image.jpg")

print( "width : {} pixels".format(img.shape[1]))
print( "height : {} pixels".format(img.shape[0]))
print( "channels : {} ".format(img.shape[2]))

(height , width) = img.shape[:2]
cv2.imshow("original Image", img)

face_cascade_name = "./harr/haarcascade_frontalface_alt.xml"
eyes_cascade_name = "./harr/haarcascade_eye_tree_eyeglasses.xml"

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

#cascade 따오기
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print("no file  x ")
    exit(0)


if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print("no file x ")
    exit(0)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()