import cv2
import numpy as np
print("Libraries Imported")

def imgProcess(path):
    img = cv2.imread(path)
    resized = cv2.resize(img,(450,300))
    kernel = np.ones((5,5),np.uint8)

    cvtd = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurd = cv2.GaussianBlur(resized, (7, 7), 0)
    canny = cv2.Canny(resized, 100, 100)
    dilated = cv2.dilate(canny, kernel, iterations=1)
    eroded = cv2.erode(resized, kernel, iterations=1)

    cv2.imshow("Resized", resized)
    cv2.imshow("Cropped", img[500:1000,500:1000])
    cv2.imshow("Gray", cvtd)
    cv2.imshow("Blured", blurd)
    cv2.imshow("Canny", canny)
    cv2.imshow("Dialated", dilated)
    cv2.imshow("Eroded", eroded)
def interImgProc(path):
    # Join
    img = cv2.resize(cv2.imread(path),(450,300))
    hor = np.hstack((img, img))
    cv2.imshow("Horizontal", hor)

def videoProcess(channel):
    cap = cv2.VideoCapture(channel)
    while True :
        success, img = cap.read()
        cv2.imshow("Captured", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def drawing():
    img = np.zeros((600,600,3),np.uint8)
    # Line
    cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,255),3)
    # Rectangle
    cv2.rectangle(img,(200,200),(400,400),(0,255,0), 3)
    # Circle
    cv2.circle(img, (300,300),100,(255,255,0),3)
    cv2.putText(img,"WISC",(300,300),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),3)
    cv2.imshow("Sketch",img)

def getPersp(path, vex):
    img = cv2.imread(path)
    width, height = 1280,720
    plane = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(vex,plane)
    imgOut = cv2.warpPerspective(img,matrix,(width,height))
    cv2.imshow("Warp", imgOut)

if __name__ == '__main__':
    # Webcam
    # videoProcess(0)
    # imgProcess("Res\\wisc.png")
    # Sketching
    # drawing()
    # Get Perspective
    # getPersp("Res\\drawing.jpg", np.float32([[335,180],[1510,210],[15,858],[1870,825]]))
    interImgProc("Res\\wisc.png")
    cv2.waitKey(0)