import cv2
import numpy as np

class control():
    def __init__(self,filtro):
      
        self.brun=True
        self.filtro= filtro
        
    def run(self):
          ##
        cam=cv2.VideoCapture(0)
        kernel=np.ones((5,5),np.uint8)
        ##variables para gui
        cv2.namedWindow('Control')
        # create trackbars for color change
        cv2.createTrackbar('PosX','Control',0,255,self.nothing)
        cv2.createTrackbar('PosY','Control',0,255,self.nothing)
        
        while (self.brun):            
            ret,frame=cam.read()          
            #opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
            #x,y,w,h= cv2.boundingRect(opening)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,),3)
            cv2.circle(frame,(cv2.getTrackbarPos('PosX','Control'),cv2.getTrackbarPos('PosY','Control')),5,(0,0,25),-1)
            # Bitwise-AND mask and original image
            #res = cv2.bitwise_and(frame,frame, mask= mask)
            #cv2.imshow('mask',mask)            
            #opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
            for value in self.filtro:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, value[0], value[1])
                opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
                x,y,w,h= cv2.boundingRect(opening)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,),3)
                cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,25),-1)

                cv2.imshow('Control',frame)            
            k=cv2.waitKey(1) & 0xff
            if k==27:
                break
        cv2.destroyAllWindows()
        del cam
   
    def exit(self):
        self.brun=False
    def nothing(self,x):
        pass
