import src.shared.constants as c
import src.core.content.contentManager as content
import src.math.vectors as v
import pygame

class game:

    def __init__(self, game):

        self.game = game

        self.circlePos = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)
    
    def run(self):

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.circlePos.y -= 300 * self.game.deltaTime
                
            if keys[pygame.K_s]:
                self.circlePos.y += 300 * self.game.deltaTime
                    
            if keys[pygame.K_a]:
                self.circlePos.x -= 300 * self.game.deltaTime

            if keys[pygame.K_d]:
                self.circlePos.x += 300 * self.game.deltaTime

            self.game.display.fill(c.Colours.BLUE)

            pygame.draw.circle(self.game.display, c.Colours.RED, self.circlePos.value(), 40)