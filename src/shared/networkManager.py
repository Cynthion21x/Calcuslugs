import socket

class Network:

    def __init__(self):
        self.client_socket = None
        self.server_socket = None
        
    def createServer(self, host, port):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()

    def connectToServer(self, server_ip, server_port):

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))

    def sendData(self, data):

        if self.client_socket:
            self.client_socket.send(data.encode())

        elif self.server_socket:
            # Broadcast data to all clients
            # Iterate through connected clients and send data
            pass
    
    def receiveData(self):

        if self.client_socket:
            return self.client_socket.recv(1024).decode()
        
        elif self.server_socket:
            # Receive data from a specific client
            pass