import socket
import selectors
import types

host, port = '127.0.0.1', 54321
sel = selectors.DefaultSelector()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen()
print("Listening")
s.setblocking(False)
sel.register(s, selectors.EVENT_READ, None)
