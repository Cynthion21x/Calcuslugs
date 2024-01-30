import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import pygame

class splashScreen:

    def __init__(self, game):

        self.game = game
        self.title = elements.photo(

            v.Vector(0, 0), v.Vector(1, 1),
            content.fetch().Sprite("Titles\\gameTitle")

            )

    def run(self):

        self.game.display.fill(c.Colours.BLUE)

        self.title.render(self.game.display)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game.GameState = c.States.GAME
