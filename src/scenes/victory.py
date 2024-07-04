import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.Input.inputManager as Input

class victory:

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

    def run(self):

        self.background.render(self.game.display)

        if self.team:

            self.WinText.render(self.game.display)

        else:

            self.LooseText.render(self.game.display)

