# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2 as cv


def nothing(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')
#Ekrandaki trackbarları oluşturur
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)
#Enable ve disable etmek için
switch='0:OFF \n 1:ON'
cv.createTrackbar(switch,'image',0,1,nothing)

while (1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    #B için trackbar değerini alır (Blue)
    b = cv.getTrackbarPos('B', 'image')
    #G için trackbar değerini alır(Green)
    g=cv.getTrackbarPos('G','image')
    #R için trackbar değerini alır (Red)
    r=cv.getTrackbarPos('R','image')

    s=cv.getTrackbarPos(switch,'image')
    #Eğer trackbardaki switch değeri sıfırsa hesaplama yapmaz
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]



#img[:]=[b,g,r]

cv.waitKey()
cv.destroyAllWindows()


