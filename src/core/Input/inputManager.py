import pygame
import src.math.vectors as v
import src.shared.logger as l

import src.shared.constants as c

class inputManager:

    def __init__(self):

        self.MOUSE_DOWN = False

        self.KEY_DOWN = c.NO_KEY
        self.KEY_HOLD = c.NO_KEY

        self.MOUSE_UP = False
        self.MOUSE_CLICK = False

        self.LETTER_DOWN = ""

        self.QUIT = False

    def gatherInput(self):

        ev = pygame.event.get()

        self.MOUSE_CLICK = False

        self.MOUSE_UP = False

        self.KEY_DOWN = c.NO_KEY

        self.LETTER_DOWN = ""

        keyHold = True

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

            if event.type == pygame.KEYDOWN:

                self.KEY_DOWN = self.KEY_HOLD = event.key

                self.LETTER_DOWN = event.unicode

            elif event.type == pygame.KEYUP:

                keyHold = False

        if keyHold == False:

            self.KEY_HOLD = c.NO_KEY


    def getMousePos(self):

        return v.FromTuple(pygame.mouse.get_pos())

  
i = inputManager()

def fetch():

    if i is None:

        l.Logger.log("Don't acess input beffore its loaded", c.Logs.WARNING)

    return i