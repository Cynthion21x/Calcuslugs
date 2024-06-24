import src.shared.constants as c
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.UI.elements as elements
import src.core.content.config as config

class game:

    def __init__(self, game):

        self.game = game

        self.circlePos = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        # TURN 1 -> PLAYER 1
        # TURN 2 -> PLAYER 2

        self.turn = 1

        self.started = False

        self.ui()
    
    def ui(self):

        self.mainBox = elements.photo(v.Zero, v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), content.Sprite("UI\\gameBox"))

    def start(self):
         
        self.started = True
        self.turnTimer = config.getOption("turnTime")

        self.player1Slugs = []
        self.player2Slugs = []

    def run(self):

        if not self.started:
            self.start()

        self.game.display.fill(c.Colours.GREY)
        self.mainBox.render(self.game.display)

