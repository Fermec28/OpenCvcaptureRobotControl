# Echo client program
import time
import socket
class carro():
    def __init__(self,host,port,filtro):
        #host es la "ip" del dispositivio
        #port es el puerto para la comunicacion (ver codigo ESP8266)
        #Filtro es un diccionario que contiene los valores para halla el carro en la imagen
        self.HOST=host
        self.PORT=port        
        self.filtro= filtro        
        # filtro["lower_filter"] = np.array([?,?,?])
        # filtro["upper_filter"] = np.array([?,?,?])

    def sendMessage(self,message):
        #crea conexion con el carro y envia los datos
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        s.sendall(message)        
        data = s.recv(1024)
        s.close()
        return data

    def mover(self,x=0,y=0):
        #establece los movimientos segun los parametros
        #x=0, y=0  moverse a x izquierda  y izquierda
        # 1: Izquierda
        # 2: quieto
        # 3: derecha
        return self.sendMessage("/x"+str(x)+"/y"+str(y)+"/")
    def closeconection(self):
        self.s.close()
        








    
    
        
