import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.Input.inputManager as Input

class splashScreen:

    def __init__(self, game):

        self.game = game

        center = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        TitleSize = v.Vector(900, 500)

        self.title = elements.photo(

            v.add(v.sub(center, v.mult(TitleSize, 0.5)), v.Vector(0, -97)), TitleSize,
            content.Sprite("Titles\\gameTitle-alt"),
            True

            )
        
        self.prompts = elements.text(

            v.sub(center, v.Vector(150, -150)), v.Vector(300, 100),
            content.Text("Text")["SplashText"],
            content.Font("Sobiscuit")

            )

    def run(self):

        self.game.display.fill(c.Colours.BACKGROUND)

        self.title.render(self.game.display)
        self.prompts.render(self.game.display)

        if Input.fetch().KEY_DOWN != c.NO_KEY:

            self.game.GameState = c.States.MENU
