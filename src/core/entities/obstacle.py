import src.math.vectors as v
import src.shared.constants as c
import pygame
import random

class obstacle:

    def __init__(self, vector, none = False):

        self.pos = vector

        self.hp = random.randint(0, 10)

        self.color = c.Colours.GREY

        self.none = none

        r = self.color.r / 2
        g = self.color.g / 2
        b = self.color.b / 2

        self.color = pygame.Color(
            int(r + ((255 - r) * (self.hp/10))/3),
            int(b + ((255 - b) * (self.hp/10))/3),
            int(g + ((255 - g) * (self.hp/10))/3)
        )

    def render(self, display):

        if not (self.none):

            pygame.draw.rect(display, self.color, pygame.Rect(self.pos.x, self.pos.y, 20, 20))

        else:

            pass
