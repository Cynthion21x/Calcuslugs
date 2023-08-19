import Game.src.shared.constants as c
import Game.src.shared.network as n

class Client:

    def __init__(self, adress, game):

        self.network = n.Network()

        ip, port = adress.split(":")

        self.network.connectToServer(ip, int(port))

        game.state = c.States.LOBBY

    def update(self):

        pass
        
    