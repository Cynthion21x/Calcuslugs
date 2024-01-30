import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import pygame

class splashScreen:

    def __init__(self, game):

        self.game = game

        center = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        TitleSize = v.Vector(900, 500)

        self.title = elements.photo(

            v.add(v.sub(center, v.mult(TitleSize, 0.5)), v.Vector(0, -60)), TitleSize,
            content.fetch().Sprite("Titles\\gameTitle-alt"),
            True

            )
        
        self.prompts = elements.text(

            v.sub(center, v.Vector(150, -150)), v.Vector(300, 100),
            "Press Enter To Start",
            content.fetch().Font("Sobiscuit")

            )

    def run(self):

        self.game.display.fill(c.Colours.BACKGROUND)

        self.title.render(self.game.display)
        self.prompts.render(self.game.display)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game.GameState = c.States.GAME
