import pygame

import src.shared.constants as c

class inputManager:

    def __init__(self, game):

        self.MOUSE_DOWN = False

        self.KEY_DOWN = c.NO_KEY