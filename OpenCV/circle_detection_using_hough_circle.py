#Kütüphanelerimiz import ettik
import numpy as np
import cv2 as cv
img=cv.imread("smarties.png")
#img=cv.VideoCapture(0)


output=img.copy()
#Resmimizi BGR DAN GRAY E çevirdik
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.medianBlur(gray,5)
#çemberleri algılamak için
circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

detected_circles=np.uint16(np.around(circles))
#Algılanan çemberlerin koordinatları yarı çapları
for(x,y,r) in detected_circles[0,:]:
    cv.circle(output,(x,y),r,(0,255,0),3)
    cv.circle(output,(x,y),2,(0,255,255),3)

cv.imshow('output',output)
cv.waitKey(0)
cv.destroyAllWindows()