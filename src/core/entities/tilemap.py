import src.core.entities.obstacle as obstacle
import src.math.vectors as v
import src.shared.constants as c
import src.shared.logger as l
import time
import math

class Tilemap:

    def __init__(self, width, height, params, colour):

        self.grid = []

        # Generator function

        l.Logger.log("Generating Terrain...")

        start = time.process_time()

        for x in range(width):

            self.grid.append([])

            for y in range(height):

                xS = x + c.GAME_WIDTH / 2

                index = (c.GAME_HEIGHT * 0.75) - (params[6] *math.sin((xS+params[3]) / params[0]) + params[7] * math.sin((xS+params[4]) / params[1]) + params[8] * math.sin((xS+params[5]) / params[2]))

                if (y > index):

                    self.grid[x].append(obstacle.obstacle(

                        v.gameToNormalCoord(v.Vector(x, y)),
                        False,
                        colour

                    ))

                else:

                    self.grid[x].append(obstacle.obstacle(

                        v.gameToNormalCoord(v.Vector(x, y)),
                        True,
                        colour

                    ))

        l.Logger.log("Generation Complete", str(math.floor((time.process_time() - start) * 100) / 100) + "s")

    def render(self, game):

        for x in range(0, len(self.grid)):

            for y in range(0, len(self.grid[x])):

                self.grid[x][y].render(game)