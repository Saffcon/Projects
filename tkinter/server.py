import socket
class server:
    def _init_(self,ip,port):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1',10502))
    def listen(self):
        self.s.listen(5)
    def accept(self):
        self.conn, addr=s.accept()
        print('connected by', addr)
    def senddata(self):
        try:
            self.conn.sendall(data)
            a=data.decode()
            if len(a)>0:
                print(a)
        except:
            conn.close()
    def receivedata(self):
        try:
            data= conn.recv(1024)
        except:
            conn.close()
p=server()
p.listen()
p.accept()
while True:
    p.recievedata()
    p.senddata()
