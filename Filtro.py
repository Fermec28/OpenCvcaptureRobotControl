import cv2
import numpy as np

class camaraa():
    def __init__(self):
      
        self.brun=True
        self.lower_filter = np.array([0,0,0])
        self.upper_filter = np.array([0,0,0])        

    def getFilter(self):
        return  np.array([self.lower_filter,self.upper_filter])  

    def run(self):
          ##
        cam=cv2.VideoCapture(0)
        kernel=np.ones((5,5),np.uint8)
        ##variables para gui
        cv2.namedWindow('Filtro')
        # create trackbars for color change
        cv2.createTrackbar('Hmax','Filtro',0,255,self.nothing)
        cv2.createTrackbar('Hmin','Filtro',0,255,self.nothing)
        cv2.createTrackbar('Smax','Filtro',0,255,self.nothing)
        cv2.createTrackbar('Smin','Filtro',0,255,self.nothing)
        cv2.createTrackbar('Vmax','Filtro',0,255,self.nothing)
        cv2.createTrackbar('Vmin','Filtro',0,255,self.nothing)
        while (self.brun):
            self.lower_filter = np.array([cv2.getTrackbarPos('Hmin','Filtro'),cv2.getTrackbarPos('Smin','Filtro'),cv2.getTrackbarPos('Vmin','Filtro')])
            self.upper_filter =np.array([cv2.getTrackbarPos('Hmax','Filtro'),cv2.getTrackbarPos('Smax','Filtro'),cv2.getTrackbarPos('Vmax','Filtro')])
            ret,frame=cam.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower_filter, self.upper_filter)
            opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
            x,y,w,h= cv2.boundingRect(opening)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,),3)
            cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,25),-1)
            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame,frame, mask= mask)
            cv2.imshow('mask',mask)            
            cv2.imshow('camara',frame)            
            k=cv2.waitKey(1) & 0xff
            if k==27:
                break
        cv2.destroyAllWindows()
        del cam
   
    def exit(self):
        self.brun=False
    def nothing(self,x):
        pass
