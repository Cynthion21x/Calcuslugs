import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.Input.inputManager as Input

class victory:

    def __init__(self, game):

        self.game = game
        self.team = True

    def run(self):

        if self.team:

            self.game.display.fill(c.Colours.BACKGROUND)

        else:

            self.game.display.fill(c.Colours.BACKGROUND)

