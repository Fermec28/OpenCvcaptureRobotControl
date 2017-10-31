import cv2
import numpy as np
def nothing(x):
    pass

##Variables para camara
cam=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)

##variables para gui
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('Hmax','image',0,255,nothing)
cv2.createTrackbar('Hmin','image',0,255,nothing)
cv2.createTrackbar('Smax','image',0,255,nothing)
cv2.createTrackbar('Smin','image',0,255,nothing)
cv2.createTrackbar('Vmax','image',0,255,nothing)
cv2.createTrackbar('Vmin','image',0,255,nothing)

lower_filter = np.array([0,0,0])
upper_filter = np.array([0,0,0])


while (True):
    lower_filter = np.array([cv2.getTrackbarPos('Hmin','image'),cv2.getTrackbarPos('Smin','image'),cv2.getTrackbarPos('Vmin','image')])
    upper_filter =np.array([cv2.getTrackbarPos('Hmax','image'),cv2.getTrackbarPos('Smax','image'),cv2.getTrackbarPos('Vmax','image')])
    ret,frame=cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_filter, upper_filter)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(1) & 0xff
    if k==27:
        break

cv2.destroyAllWindows()
del cam 
