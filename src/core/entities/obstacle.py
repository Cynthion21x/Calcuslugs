import src.math.vectors as v
import src.shared.constants as c
import pygame
import random

class obstacle:

    def __init__(self, vector, none = False, colour = c.Colours.FLOOR):

        self.pos = vector

        self.hp = random.randint(0, 10)

        self.color = colour

        self.none = none

        r = self.color[0]
        g = self.color[1]
        b = self.color[2]

        r *= c.Colours.FLOOR.r
        g *= c.Colours.FLOOR.g
        b *= c.Colours.FLOOR.b

        r /= 255
        g /= 255
        b /= 255

        self.color = pygame.Color(
            int(r),
            int(g),
            int(b)
        )

    def render(self, display):

        if not (self.none):

            pygame.draw.rect(display, self.color, pygame.Rect(self.pos.x, self.pos.y, c.TILE_SIZE, c.TILE_SIZE))

        else:

            pass
