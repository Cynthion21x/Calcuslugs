import threading
import socket
import Game.src.shared.constants as c
import Game.src.shared.network as n

class Server:

    def __init__(self, port, game):

        self.network = n.Network()

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.serverSocket.bind((c.LOCALHOST, int(port)))
        except socket.error as e:
            str(e)

        self.serverSocket.listen(2)

        self.gamestate = c.States.LOBBY

        self.players = []

        