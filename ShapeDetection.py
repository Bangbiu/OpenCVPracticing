import cv2
import numpy as np

print("Libraries Imported")

def getBoundingBox(img, overlay):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        peri = cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
        if approx.shape[0] == 4:
            print(approx.reshape(4,2))
        cv2.polylines(overlay,approx,True,(255,0,0),5)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(overlay,(x,y),(x+w,y+h),(0,0,0),1)
    return overlay

def getContour(img,overlay):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:

        if (cv2.contourArea(cont) > 50):
            # print(cv2.contourArea(cont))
            peri = cv2.arcLength(cont,True)
            approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
            objCor = len(approx)
            #print(approx[0,0])
            cv2.putText (overlay,str(objCor),approx[0,0],cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,255),1)
            cv2.drawContours(overlay, cont, -1, (255, 0, 255), 2)
    return overlay

img = cv2.imread("Res\\shapes.png")
img = cv2.resize(img,(400,400))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2RGB)
imgBlur = cv2.GaussianBlur(imgGray,(7, 7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgCont = getContour(imgCanny,img.copy())
imgBound = getBoundingBox(imgCanny,img.copy())
imgCanny = cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2RGB)
cv2.imshow("Image",np.vstack((np.hstack((img,imgGray,imgBlur)),np.hstack((imgCanny,imgCont,imgBound)))))

cv2.waitKey(0)