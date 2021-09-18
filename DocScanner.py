import cv2
import numpy as np

def reorder (myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    #print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    #print("NewPoints",myPointsNew)
    return myPointsNew

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.resize(img,(320,240))
    # cpd = img[180:640,180:480]
    imgCont = img.copy()
    imgBlur = cv2.GaussianBlur(img,(7, 7),1)
    imgCanny = cv2.Canny(imgBlur,300,50)
    imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)
    imgPers = np.zeros((240,240,3),np.uint8)
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:

        if (cv2.contourArea(cont) > 200):
            # print(cv2.contourArea(cont))
            peri = cv2.arcLength(cont, True)
            approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
            objCor = len(approx)
            # print(approx[0,0])
            # cv2.putText(imgCont, str(objCor), approx[0, 0], cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 1)
            cv2.drawContours(imgCont, cont, -1, (255, 0, 255), 2)
            cv2.polylines(imgCont, approx, True, (255, 255, 0), 3)


            if objCor == 4:
                width, height = 240, 240
                persp = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
                approx = np.float32(reorder(approx))
                matrix = cv2.getPerspectiveTransform(approx, persp)
                imgPers = cv2.warpPerspective(img, matrix, (width, height))



    imgDilate = cv2.cvtColor(imgDilate, cv2.COLOR_GRAY2RGB)

    cv2.imshow("Captured", np.hstack((imgDilate,imgCont,imgPers)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

