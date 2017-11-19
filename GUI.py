from Tkinter import *
import cv2
from Filtro import camaraa
#from Control import control
import numpy as np
import threading

class Application(Frame):

    boolfiltro=False
    boolcontrol=False
    varfiltro=[]     
    def save(self):
        if (self.boolfiltro):
            self.varfiltro.append(self.track.getFilter())
            self.track.exit()
            self.boolfiltro=False
            print self.varfiltro
        print "Vamos a guardar los datos del filtro..."       
    
        
    def find_filter(self):
        print "Iniciando la Busqueda del Flitro..."        
        if (not(self.boolfiltro)):
            self.boolfiltro=True
            t = threading.Thread(target=self.filtro)
            t.start()

    def filtro(self):        
        self.track= camaraa()
        self.track.run()

    def condicionesi(self):
        print "Aqui setearemos los robots..."

    def control(self):
        print "Aqui controlaremos los robots "           
        if (not(self.boolcontrol)):
            self.boolcontrol=True
            t = threading.Thread(target=self.controlcallback)
            t.start()
            
    def controlcallback (self):
        self.controlador= control(self.varfiltro)
        self.controlador.run()
        

    def exitt(self):
        print "Chao dice la aplicacion"
        if (self.boolfiltro):
            self.track.exit()
        if (self.boolcontrol):
             self.controlador.exit()
        self.quit        
        root.destroy()
        
    def createWidgets(self):  
        self.hi_there = Button(self)
        self.hi_there["text"] = "NUEVO FILTRO"
        self.hi_there["command"] = self.find_filter

        self.hi_there.pack({"side": "left"})

        self.SAVE = Button(self)
        self.SAVE["text"] = "Guardar"
        self.SAVE["fg"]   = "blue"
        self.SAVE["command"] =self.save

        self.SAVE.pack({"side": "left"})


        self.SAVE = Button(self)
        self.SAVE["text"] = "Condiciones Iniciales"
        self.SAVE["fg"]   = "orange"
        self.SAVE["command"] =self.condicionesi

        self.SAVE.pack({"side": "left"})

        self.CONTROL = Button(self)
        self.CONTROL["text"] = "Iniciar Control"
        self.CONTROL["fg"]   = "green"
        self.CONTROL["command"] = self.control

        self.CONTROL.pack({"side": "left"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "SALIR"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =self.exitt

        self.QUIT.pack({"side": "left"})      

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
