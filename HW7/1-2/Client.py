import socket            
 
s = socket.socket()        
 
port = 12345               
 
s.connect(('127.0.0.1', port))

f = open("data_cli.txt", "w")
for i in range(2):
    f.write(s.recv(1024).decode())
f.close()

s.close()    