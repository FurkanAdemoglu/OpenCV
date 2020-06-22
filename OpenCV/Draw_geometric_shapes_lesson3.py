import numpy as np
import cv2
#Resmimizi Yükledik
img=cv2.imread('lena.jpg',1)
#ilk Parametre hangi resim oldupunu söyler sonraki ikili iki parametre koordinatlardır üçlü parametre renk diğeri ise kalınlık
#Resimin üstüne çizgi çimemize yarar
img=cv2.line(img,(0,0),(255,255),(147,96,44),10)
#Resmin üstüne yönlü ok çizmemize yarar
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)
#Resime kare çimemize yarar
img=cv2.rectangle(img,(384,0),(512,128),(0,0,255),10)
#RESİME DAİRE ÇİZER
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
#Resmin üstüne yazılacak yazının fontu
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
#Resmin üstüne yazı yazmaya yarar
img=cv2.putText(img,'OpenCv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()