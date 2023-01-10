import socket            
 
s = socket.socket()        
 
port = 12345               
 
s.connect(('127.0.0.1', port))

write = False;

while True:
    str = s.recv(1024).decode();
    if(write):
        f = open("data_cli.txt", "w")
        for i in range(2):
            f.write(str)
            str = s.recv(1024).decode();
        f.close()
        break;
    if(str == ''):
        continue;
    print(str)
    if(str == 'Write begins'):
        write = True;
    if(str[-1]=='?'):
        x = input();
        s.send(x.encode())

s.close()    