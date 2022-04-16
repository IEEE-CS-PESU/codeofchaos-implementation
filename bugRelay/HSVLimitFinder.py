
import cv2
import numpy as np


def empty(a): 
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


cv2.namedWindow('Trackbars')  
cv2.resizeWindow('Trackbars', 640, 240)

cv2.createTrackbar('H minimum', 'Trackbars', 0, 255, empty)  
cv2.createTrackbar('H maximum', 'Trackbars', 179, 179, empty)
cv2.createTrackbar('S minimum', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('S maximum', 'Trackbars', 255, 255, empty)
cv2.createTrackbar('V minimum', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('V maximum', 'Trackbars', 255, 255, empty)

while True:

    img = cv2.imread('doge.png') # the participants are supposed to change the path to any available picture on their computer
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # the macro 'cv2.COLOR_BGR2HSV' was changed to 'cv2.COLOR_BGR2GRAY'

    hMin = cv2.getTrackbarPos('H minimum', 'Trackbars')
    hMax = cv2.getTrackbarPos('H maximum', 'Trackbars')
    sMin = cv2.getTrackbarPos('S maximum', 'Trackbars')
    sMax = cv2.getTrackbarPos('S maximum', 'Trackbars')
    vMin = cv2.getTrackbarPos('V minimum', 'Trackbars')
    vMax = cv2.getTrackbarPos('V maximum', 'Trackbars')
   

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])  
    mask = cv2.inRange(imgHSV, lower, upper) 
    imgResult = cv2.bitwise_and(img, img,mask=mask)  

    imgStacked = stackImages('0.5', ([img, mask, imgResult])) # 0.5 shouldn't be enclosed in quotes. It is intended to be supplied as a float value

    cv2.imshow('Test window', img) # 'imgStacked' was changed to 'img'. This is a runtime error and won't throw any exceptions

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print()
print('Required values : ')
print('hMin, sMin, vMin, hMax, sMax, vMax = ', hMin, ',', sMin, ',', vMin, ',', hMax, ',', sMax, ',', vMax)
