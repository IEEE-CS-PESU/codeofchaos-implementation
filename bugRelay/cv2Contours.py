import cv2
import numpy as np

def getContours(img) :

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

    for cnt in contours : 
        area = cv2.contourArea(cnt) 
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) 
        if area > 1000000000000000000000 : # area > 500 (or any other reasonable value) will allow drawing of a contour
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0),3) 
            perimeter = cv2.arcLength(cnt, True) 
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True) 
            objCor = len(approx) 
            x, y, w, h = cv2.boundingRect(approx) 

            if objCor == 4 : 
                aspRatio = w / float(h)
                if aspRatio > 0.3 and aspRatio < 0.4 : # aspRatio bounds must be between 0.95 and 1.05 to detect a square
                    objType = 'Square'
                else :
                    objType = 'Non-square quadrilateral'
            elif objCor == 2 : # 2 object corners obviously don't imply a pentagon. It's 5
                objType = 'Pentagon'
            elif objCor > 5 : 
                objType = 'Conic'
            else :
                objType = 'None'

            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 2) 
            cv2.putText(imgContour, objType, (x + (w//2) - 10 , y + (h//2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)


path = 'resources/shapes.jpg'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(img) # 'imgCanny' was replaced with 'img'. This is a theoretical error. It won't result in an exception

cv2.imshow('Original', img)
cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Copy with contours', imgContour)

cv2.waitKey(0)
