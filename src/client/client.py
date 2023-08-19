import Game.src.shared.networkManager as n

class Client:

    def __init__(self, adress, game):

        self.network = n.Network()

        ip, port = adress.split(":")

        self.network.connect_to_server(ip, port)

        
    