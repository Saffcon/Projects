import threading
from threading import Thread
import os
global ip
global port
global s
global f

c=[]
threads=[]
def socket():
   # try:
    import socket
    global f
    ip='localhost'
    port=9995
    filename='ip.txt'
    mode='w'
    f=Filefunction(filename,mode)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    return s
    '''except:
        print('a')
        for connection in c:
            connection.close()
        s.close()'''

class Filefunction():
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.iplist=[]
    def writefile(self,a):
        with open(self.filename,'w') as file:
            file.write(a)
    def readfile(self):
        with open(self.filename,'r') as file:
            for line in file:
                self.iplist.append(line)
        return self.iplist
    def appendfile(self,x):     
        with open(self.filename,'a') as file:
                  file.write(x) 
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
        global f
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.conn=conn
        f.writefile(ip+':'+str(port))
        
        print('[+] New server socket thread started for'+ip+':'+str(port))
    def run(self):
        while 1:
            data=conn.recv(10000)
            print('server recieved data:', data)
            print('Multithreaded Python server: Waiting for connections from TCP listens...')
            for a in c:
                a.send(data)
                time.sleep(0.01)
    def sendip(self):
        while 1:
            i=f.readfile()
            k=','.join(i)
            if k!='':
                k=k.encode()
                for a in c:
                    a.send(k)
        def recieve(self):
            print('adsde')
            while 1:
                for a in c:
                    message=a.recv(1024)
                    if data!=b'':
                        print('server recieved message:'+message)
        
            
s=socket()
def create_thread(conn,c):
    t=ClientThread(ip,port,conn)
    rt=ClientThread(ip,port,conn)
    c.append(conn)
    t.sendip()
    rt.recieve()
    
while 1:
    (conn,(ip,port))=s.accept()
    t1=threading.Thread(target=create_thread, args=(conn,c))
    rt=threading.Thread(target=create_thread, args=(conn,c))
    t1.start()
    rt.start()
    threads.append(t1)


