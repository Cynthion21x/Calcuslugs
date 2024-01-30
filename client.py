import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 16090))
while True:
    str = input("S: ")
    s.send(str.encode());

s.close()
