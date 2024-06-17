import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.shared.logger as l

class mainMenu:

    def startButtonFunc(self):

        self.game.GameState = c.States.GAME

    def __init__(self, game):

        self.game = game

        center = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        buttonSize = v.Vector(200, 100)

        buttonX = center.x - (buttonSize.x / 2)
        buttonY = 20

        startButtonNorm = elements.photo(
            v.Vector(buttonX, buttonY),
            buttonSize,
            content.Sprite("UI\\button")
        )

        hoverScale = 1.2
        startButtonHover = elements.photo(

            v.Vector(center.x - (buttonSize.x * hoverScale / 2), buttonY - (buttonSize.y * hoverScale - buttonSize.y) / 2),
            v.mult(buttonSize, 1.2), 
            content.Sprite("UI\\button-hover")

        )

        startButton = elements.button(v.Vector(buttonX, 20), buttonSize, self.startButtonFunc, startButtonNorm, startButtonHover)

        startButtonText = elements.text(

            v.Vector(center.x - (buttonSize.x * 0.8 / 2), buttonY + 5 - (buttonSize.y * 0.8 - buttonSize.y) / 2),
            v.mult(buttonSize, 0.8),
            content.Text("menuText")["PlayButton"],
            content.Font("Sobiscuit")

        )

        self.background = elements.photo(
            v.Vector(0, 0),
            v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT),
            content.Sprite("UI\\mainMenubg")
        )

        self.mainButtons = elements.group([

            startButton,
            startButtonText

        ])

    def run(self):

        self.background.render(self.game.display)
        self.mainButtons.run(self.game.display)