import src.core.entities.obstacle as obstacle
import src.math.vectors as v
import math

class Tilemap:

    def __init__(self, width, height, params):

        self.grid = []

        # Generator function

        for x in range(width):

            self.grid.append([])

            for y in range(height):

                index = 10 - math.sin((x+params[4]) / params[0]) + math.sin((x+params[5]) / params[1]) + math.sin((x+params[6]) / params[3])

                if (y > index):

                    self.grid[x].append(obstacle.obstacle(

                        v.gameToNormalCoord(v.Vector(x, y)),
                        False

                    ))

                else:

                    self.grid[x].append(obstacle.obstacle(

                        v.gameToNormalCoord(v.Vector(x, y)),
                        True

                    ))   

    def render(self, game):

        for x in range(0, len(self.grid)):

            for y in range(0, len(self.grid[x])):

                self.grid[x][y].render(game)