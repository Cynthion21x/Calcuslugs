import pygame
import src.math.vectors as v
import src.shared.logger as l

import src.shared.constants as c

class inputManager:

    def __init__(self):

        self.MOUSE_DOWN = False

        self.KEY_DOWN = c.NO_KEY

        self.MOUSE_UP = False
        self.MOUSE_CLICK = False

        self.QUIT = False

    def gatherInput(self):

        ev = pygame.event.get()

        self.MOUSE_CLICK = False
        self.MOUSE_DOWN = False

        self.KEY_DOWN = c.NO_KEY

        for event in ev:

            if event.type == pygame.QUIT:

                self.QUIT = True

            else:

                self.QUIT = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                self.MOUSE_DOWN = True
                self.MOUSE_CLICK = True

            elif event.type == pygame.MOUSEBUTTONUP:

                self.MOUSE_DOWN = False
                self.MOUSE_UP = True

            if event.type == 768:

                self.KEY_DOWN = event.key


    def getMousePos(self):

        return v.FromTuple(pygame.mouse.get_pos())
  
i = inputManager()

def fetch():

    if i == None:

        l.Logger.log("Don't acess input beffore its loaded", c.Logs.WARNING)

    return i