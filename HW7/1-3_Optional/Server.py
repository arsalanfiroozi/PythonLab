import socket
import threading


def coder(s, c, addr):
    print('Got connection from', addr)
    c.send('Which data to be sent? 1 or 2?'.encode())
    num = c.recv(1024).decode()
    print(num)

    c.send('Write begins'.encode())
    f = open("data"+num+".txt", "r")
    for x in f:
        c.send(x.encode())

    print('Data sent for ', addr)

    c.close();
    return


threads = []


s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()

    t = threading.Thread(target=coder, args=(s, c, addr))
    threads.append(t)
    t.start()

    # break
