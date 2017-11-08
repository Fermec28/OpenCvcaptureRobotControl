# Echo client program
import socket
class carro():
    def _init_(self,host,port):
        self.HOST=host
        self.PORT=port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMessage(self,message):
        self.s.connect((HOST, PORT))
        self.s.sendall('Hello, world')
        data = s.recv(1024)
        self.s.close()
        print 'Received', repr(data)
        
