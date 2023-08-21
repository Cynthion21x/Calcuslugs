import threading
import socket
import pickle
import Game.src.shared.constants as c

class Server:

    def __init__(self, port, game):

        self.port = int(port)

        self.running = False

        server_thread = threading.Thread(target=self.serverThread)
        server_thread.start()

    def serverThread(self):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind((c.LOCALHOST, self.port))
        self.server.listen(4)

        print("Server hosted on port " + str(self.port) + " Waiting for players...")

        while self.running:
            client_socket, client_address = self.server.accept()
            print("Player connected:", client_address)

        self.server.close()

    def exit(self):

        self.running = False

        print("Shutting off the server")
        