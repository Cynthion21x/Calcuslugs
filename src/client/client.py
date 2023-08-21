import socket
import threading
import Game.src.shared.constants as c

class Client:

    def __init__(self, adress, game):

        self.ip, self.port = adress.split(":")

        self.port = int(self.port)

        self.game = game

    def join(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.ip, self.port))
        print("Connected to server.")

        self.game.state = c.States.LOBBY
    