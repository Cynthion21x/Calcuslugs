import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.shared.logger as l

class mainMenu:

    def startButtonFunc(self):

        self.game.GameState = c.States.GAME

    def optionButtonFunc(self):

        pass

    def quitButtonFunc(self):

        self.game.exit()

    def __init__(self, game):

        self.game = game

        center = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        buttonSize = v.Vector(200, 100)

        buttonX = center.x - (buttonSize.x / 2)
        buttonY = 40

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

        optionButtonHover = elements.photo(
            v.Vector(center.x - (buttonSize.x * hoverScale / 2), buttonY + 190 - ((buttonSize.y * hoverScale - buttonSize.y) / 2)),
            v.mult(buttonSize, 1.2), 
            content.Sprite("UI\\button-hover")
        )

        optionButton = elements.photo(
            v.Vector(buttonX, buttonY + 190),
            buttonSize,
            content.Sprite("UI\\button")
        )

        exitButtonNorm = elements.photo(
            v.Vector(buttonX, buttonY + 390),
            buttonSize,
            content.Sprite("UI\\button")
        )

        exitButtonHover = elements.photo(
            v.Vector(center.x - (buttonSize.x * hoverScale / 2), buttonY + 390 - ((buttonSize.y * hoverScale - buttonSize.y) / 2)),
            v.mult(buttonSize, 1.2), 
            content.Sprite("UI\\button-hover")
        )

        startButton = elements.button(v.Vector(buttonX, buttonY), buttonSize, self.startButtonFunc, startButtonNorm, startButtonHover)
        
        optionButton = elements.button(v.Vector(buttonX, buttonY + 190), buttonSize, self.optionButtonFunc, optionButton, optionButtonHover)

        exitButton = elements.button(v.Vector(buttonX, buttonY + 380), buttonSize, self.quitButtonFunc, exitButtonNorm, exitButtonHover)

        startButtonText = elements.text(

            v.Vector(center.x - (buttonSize.x * 0.8 / 2), buttonY + 5 - (buttonSize.y * 0.8 - buttonSize.y) / 2),
            v.mult(buttonSize, 0.8),
            content.Text("Text")["PlayButton"],
            content.Font("Sobiscuit")

        )

        opButtonText = elements.text(

            v.Vector(center.x - (buttonSize.x * 0.8 / 2), buttonY + 195 - ((buttonSize.y + 190) * 0.8 - (buttonSize.y + 190)) / 2),
            v.mult(buttonSize, 0.8),
            content.Text("Text")["OptionsButton"],
            content.Font("Sobiscuit")

        )

        exitButtonText = elements.text(

            v.Vector(center.x - (buttonSize.x * 0.8 / 2), buttonY + 385 + (buttonSize.y * 0.8) / 4),
            v.mult(buttonSize, 0.8),
            content.Text("Text")["QuitButton"],
            content.Font("Sobiscuit")

        )

        self.background = elements.photo(
            v.Vector(0, 0),
            v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT),
            content.Sprite("UI\\mainMenubg")
        )

        self.mainButtons = elements.group([

            startButton,
            startButtonText,
            optionButton,
            opButtonText,
            exitButton,
            exitButtonText

        ])

    def run(self):

        self.background.render(self.game.display)
        self.mainButtons.run(self.game.display)