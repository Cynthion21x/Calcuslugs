import socket

s = socket.socket()
s.connect(('127.0.0.1',12345))
while True:
    str = input("S: ")
    s.send(str.encode());

s.close()