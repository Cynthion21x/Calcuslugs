import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.shared.logger as l

def startButtonFunc():

    l.Logger.log("Pressed button")

class mainMenu:

    def __init__(self, game):

        self.game = game

        center = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        buttonSize = v.Vector(200, 100)

        buttonX = center.x - (buttonSize.x / 2)

        startButtonNorm = elements.photo(
            v.Vector(buttonX, 20),
            buttonSize,
            content.Sprite("UI\\button")
        )

        startButtonHover = elements.photo(
            v.Vector(center.x - (buttonSize.x * 1.2 / 2), 20),
            v.mult(buttonSize, 1.2), 
            content.Sprite("UI\\button-hover")
        )

        startButton = elements.button(v.Vector(buttonX, 20), buttonSize, startButtonFunc, startButtonNorm, startButtonHover)

        self.mainButtons = elements.group([

            startButton

        ])

    def run(self):

        self.mainButtons.run(self.game.display)