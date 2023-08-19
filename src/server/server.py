import Game.src.shared.networkManager as n

class Server:

    def __init__(self, port, game):

        self.network = n.Network()
        self.network.create_server('127.0.0.1', int(port))

    
        