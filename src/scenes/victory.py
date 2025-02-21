import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.Input.inputManager as Input

class victory:

    def backButtonFunc(self):

        self.game.GameState = c.States.MENU

    def playAgainButtonFunc(self):

        self.game.GameState = c.States.GAME

    def __init__(self, game):

        self.game = game
        self.team = True

        self.background = elements.photo(v.Zero, v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), content.Sprite("UI\\looseScreen"))

        self.WinText = elements.text(

            v.mult(v.Vector(c.SCREEN_WIDTH-500, c.SCREEN_HEIGHT-250), 0.5),
            v.Vector(500, 500),
            content.Text("Text")["player1Win"],
            content.Font("Sobiscuit")

        )

        self.LooseText = elements.text(

            v.mult(v.Vector(c.SCREEN_WIDTH-500, c.SCREEN_HEIGHT-250), 0.5),
            v.Vector(500, 500),
            content.Text("Text")["player2Win"],
            content.Font("Sobiscuit")

        )

        center = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        buttonSize = v.Vector(200, 100)

        buttonX = center.x - (buttonSize.x / 2)
        buttonY = 300

        backButtonNorm = elements.photo(
            v.Vector(buttonX, buttonY),
            buttonSize,
            content.Sprite("UI\\button")
        )

        hoverScale = 1.2
        backButtonHover = elements.photo(

            v.Vector(center.x - (buttonSize.x * hoverScale / 2), buttonY - (buttonSize.y * hoverScale - buttonSize.y) / 2),
            v.mult(buttonSize, 1.2), 
            content.Sprite("UI\\button-hover")

        )

        self.backButton = elements.button(v.Vector(buttonX, buttonY), buttonSize, self.backButtonFunc, backButtonNorm, backButtonHover)

        self.backButtonText = elements.text(

            v.Vector(center.x - (buttonSize.x * 0.8 / 2), buttonY + 20 - (buttonSize.y * 0.8 - buttonSize.y) / 2),
            v.mult(buttonSize, 0.8),
            content.Text("Text")["BackButton"],
            content.Font("Sobiscuit")

        )

        buttonY = 430

        againButtonNorm = elements.photo(
            v.Vector(buttonX, buttonY),
            buttonSize,
            content.Sprite("UI\\button")
        )

        againButtonHover = elements.photo(

            v.Vector(center.x - (buttonSize.x * hoverScale / 2), buttonY - (buttonSize.y * hoverScale - buttonSize.y) / 2),
            v.mult(buttonSize, 1.2), 
            content.Sprite("UI\\button-hover")

        )

        self.againButton = elements.button(v.Vector(buttonX, buttonY), buttonSize, self.playAgainButtonFunc, againButtonNorm, againButtonHover)

        self.againButtonText = elements.text(

            v.Vector(center.x - (buttonSize.x * 0.8 / 2), buttonY + 20 - (buttonSize.y * 0.8 - buttonSize.y) / 2),
            v.mult(buttonSize, 0.8),
            content.Text("Text")["PlayAgainButton"],
            content.Font("Sobiscuit")

        )

    def run(self):

        self.background.render(self.game.display)
        self.backButton.run()
        self.backButton.render(self.game.display)
        self.backButtonText.render(self.game.display)

        self.againButton.run()
        self.againButton.render(self.game.display)
        self.againButtonText.render(self.game.display)   

        if self.team:

            self.WinText.render(self.game.display)

        else:

            self.LooseText.render(self.game.display)

