import socket
host= '127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr=s.accept()
print('connected by', addr)
while True:
    data= conn.recv(1024)
    if not data: break
    conn.sendall(data)
    print((data))
conn.close()

