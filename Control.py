##Programa que realiza el control de los robots
#instancia los objetos de los robost teniendo en cuenta su ip puerto y filtro
import cv2
import numpy as np
from Carro import carro 

class control():

    def __init__(self):
      
        self.brun=True
        fitrocarro1={'lower_filter': np.array([0, 0, 0]), 'upper_filter': np.array([255, 255, 255])}
        fitrocarro2={'lower_filter': np.array([0, 0, 0]), 'upper_filter': np.array([0, 0, 0])}
        carro1= carro('',80,fitrocarro1)
        carro2= carro('',80,fitrocarro2)
        self.carros=[carro1,carro2]
    
        
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
            for carro in self.carros:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, carro.filtro["lower_filter"], carro.filtro["upper_filter"])
                opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
                x,y,w,h= cv2.boundingRect(opening)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,),3)
                cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,25),-1)
                cv2.imshow('Control',frame)            
            k=cv2.waitKey(1) & 0xff
            if k==27:
                break
        self.brun=False
        cv2.destroyAllWindows()
        del cam
   
    def exit(self):
        self.brun=False
    def nothing(self,x):
        pass

controlador= control()                
controlador.run()
        
