import cv2
import numpy as np

print("Libraries Imported")

hueMin = 0
hueMax = 179
satMin = 0
satMax = 255
valMin = 0
valMax = 255

path = "Res\\airplane.jfif"
img = cv2.imread(path)
img = cv2.resize(img,(400,400))
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def onRangeChange(NULL):
    hueMin = cv2.getTrackbarPos("Hue Min", "TrackBars")
    hueMax = cv2.getTrackbarPos("Hue Max", "TrackBars")
    satMin = cv2.getTrackbarPos("Sat Min", "TrackBars")
    satMax = cv2.getTrackbarPos("Sat Max", "TrackBars")
    valMin = cv2.getTrackbarPos("Val Min", "TrackBars")
    valMax = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([hueMin,satMin,valMin])
    upper = np.array([hueMax,satMax,valMax])
    mask = cv2.inRange(imgHSV,lower,upper)
    res = cv2.bitwise_and(img,img,mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    cv2.imshow("Result", np.vstack((np.hstack((img,imgHSV)),np.hstack((mask,res)))))


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",(640,240))
cv2.createTrackbar("Hue Min", "TrackBars",0,179,onRangeChange)
cv2.createTrackbar("Hue Max", "TrackBars",70,179,onRangeChange)
cv2.createTrackbar("Sat Min", "TrackBars",16,255,onRangeChange)
cv2.createTrackbar("Sat Max", "TrackBars",255,255,onRangeChange)
cv2.createTrackbar("Val Min", "TrackBars",180,255,onRangeChange)
cv2.createTrackbar("Val Max", "TrackBars",255,255,onRangeChange)
onRangeChange("")



cv2.waitKey(0)

