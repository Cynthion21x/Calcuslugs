import socket

class Network:

    def __init__(self):

        self.client_socket = None
        
    def connectToServer(self, server_ip, server_port: int):

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client_socket.connect((server_ip, server_port))
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
