import src.shared.constants as c
import src.core.UI.elements as elements
import src.core.content.contentManager as content
import src.math.vectors as v
import pygame

class splashScreen:

    def __init__(self, game):

        self.game = game

        center = v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT).multC(0.5)
        size = v.Vector(200, 200)

        self.title = elements.photo(

            center.add(size.multC(-0.5)), v.Vector(200, 200),
            content.fetch().Sprite("Titles\\gameTitle")

            )

    def run(self):

        self.game.display.fill(c.Colours.BACKGROUND)

        self.title.render(self.game.display)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game.GameState = c.States.GAME
