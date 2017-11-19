import cv2
import numpy as np
from Carro import carro
from threading import Thread

def enviar(car):
##    Worker
    while(boolsendcar):
        car.mover(cv2.getTrackbarPos('Xmove','image'),cv2.getTrackbarPos('Ymove','image'))           

    
def nothing(x):
    pass



#variables para el worker
boolsendcar=True;
##Set del Carro
fitrocarro={'lower_filter': np.array([0, 0, 0]), 'upper_filter': np.array([255, 255, 255])}
car= carro('192.168.1.5',80,fitrocarro)

##Variables para camara
cam=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)

##variables para gui
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('Xmove','image',1,3,nothing)
cv2.createTrackbar('Ymove','image',1,3,nothing)

subproceso = Thread(target=enviar, args=(car,))
subproceso.start()
while (True):
    ret,frame=cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, car.filtro["lower_filter"], car.filtro["upper_filter"])

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)    
    
    
    k=cv2.waitKey(1) & 0xff
    if k==27:
        break
boolsendcar= False
cv2.destroyAllWindows()
del cam




