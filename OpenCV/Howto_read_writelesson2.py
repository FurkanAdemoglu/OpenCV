import cv2

#Kamerayı açar
cap=cv2.VideoCapture(0);

#Kamerayla çekilen videoyu kaydeder
fourcc=cv2.VideoWriter.fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(500,500))
#True yerine cap.isOpened() da olabilir
while(True):
    ret,frame=cap.read()
    if ret ==True:

        #Kameradan çekilen video ekranının genişliğini verir
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #Yüksekliğini verir
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        #Kameranın çektiği video yu gri ton yapar
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Ekranda kameradan gelen anlık görüntüyü gösterir
        cv2.imshow('Frame',gray)
#q ya basarsan program durur
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()