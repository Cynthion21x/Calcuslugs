import src.shared.constants as c
import src.core.content.contentManager as content
import src.math.vectors as v
import pygame

class game:

    def __init__(self, game):

        self.game = game

        self.circlePos = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        # TURN 1 -> PLAYER 1
        # TURN 2 -> PLAYER 2

        self.turn = 1

        self.start()
    
    def start(self):
         
        self.player1Slugs = []
        self.player2Slugs = []

    def run(self):

        self.game.display.fill(c.Colours.BLACK)

