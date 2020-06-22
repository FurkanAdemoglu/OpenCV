import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,700)#Kameranın özelliğine göre maksimum olabileceği bellidir örneğin 1280*720
#cap.set(4,700)

#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #fontu ayarlar
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='Width:'+str(cap.get(3))+'Height:'+str(cap.get(4))
        date=str(datetime.datetime.now())
        #Ekrana yazı yazdırır
        frame=cv2.putText(frame,date,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        #q tuşu ile çıkmaya yarar
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()









