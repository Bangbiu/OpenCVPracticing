import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Res\\haarcascade_frontalface_default.xml")

img1 = cv2.imread("Res\\photo1.jpg")
imgGray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("Res\\photo2.jpg")
imgGray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray2,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img2,(x,y),(x+w,y+h),(255,255,0),3)
    cv2.putText(img2, "idiot",(x,y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

cv2.imshow("Face",img2)
cv2.waitKey(0)