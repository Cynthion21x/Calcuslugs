import src.shared.constants as c
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.UI.elements as elements
import src.core.content.config as config
import time

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
        self.clock = elements.text(

            v.Vector((c.SCREEN_WIDTH - 200) / 2, 10),
            v.Vector(200, 10), "10:00",
            content.Font("Sobiscuit")

        )

    def start(self):
         
        self.started = True
        self.turnTimer = int(config.getOption("turnTime"))

        self.player1Slugs = []
        self.player2Slugs = []

    def run(self):

        if not self.started:
            self.start()

        self.turnTimer -= self.game.deltaTime

        clockText = str(int(self.turnTimer // 60))
        clockSecond = str(int(self.turnTimer % 60))

        if len(clockSecond) == 1:

            clockSecond = "0" + clockSecond

        if len(clockText) == 1:

            clockText = "0" + clockText

        self.clock.updateText(clockText + ":" + clockSecond)

        if self.turnTimer < 0:

            self.turnTimer = 0

        self.game.display.fill(c.Colours.GREY)
        self.mainBox.render(self.game.display)
        self.clock.render(self.game.display)

