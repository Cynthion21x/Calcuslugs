import src.core.entities.obstacle as obstacle
import src.math.vectors as v
import src.shared.constants as c
import src.shared.logger as l
import pygame
import time
import math

class Tilemap:

    def __init__(self, width, height, params, colour):

        self.grid = []

        self.params = params

        # Generator function

        l.Logger.log("Generating Terrain...")

        start = time.process_time()

        for x in range(width):

            self.grid.append([])

            for y in range(height):

                xS = x + c.GAME_WIDTH / 2

                index = self.mapFunc(xS)

                if (y > index):

                    self.grid[x].append(obstacle.obstacle(

                        v.gameToNormalCoord(v.Vector(x, y)),
                        False,
                        False,
                        colour

                    ))

                else:

                    if y < (c.GAME_HEIGHT / 1.1):

                        self.grid[x].append(obstacle.obstacle(

                            v.gameToNormalCoord(v.Vector(x, y)),
                            True,
                            False,
                            colour

                        ))

                    else:
                    
                        self.grid[x].append(obstacle.obstacle(

                            v.gameToNormalCoord(v.Vector(x, y)),
                            False,
                            True,
                            colour

                        ))

        l.Logger.log("Generation Complete", str(math.floor((time.process_time() - start) * 100) / 100) + "s")

        self.generatePhoto()

    def mapFunc(self, xS):

        return (c.GAME_HEIGHT * 0.75) - (self.params[6] *math.sin((xS+self.params[3]) / self.params[0]) + self.params[7] * math.sin((xS+self.params[4]) / self.params[1]) + self.params[8] * math.sin((xS+self.params[5]) / self.params[2]))

    def generatePhoto(self):

        l.Logger.log("Generating New Terrain Image...")

        start = time.process_time()

        self.image = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.SRCALPHA, 32)
        
        for x in range(0, len(self.grid)):

            for y in range(0, len(self.grid[x])):

                self.grid[x][y].render(self.image)

        self.image.convert_alpha()

        l.Logger.log("Generation Complete", str(math.floor((time.process_time() - start) * 100) / 100) + "s")

    def render(self, display):

        display.blit(self.image, (0, 0))