import pygame
import src.core.inputManager as inputManager
import src.core.content.contentManager as content
import src.shared.constants as c
import src.shared.logger as l

class Game():

    def __init__(self, message):

        pygame.init()

        self.message = message

        self.running = True

        self.display = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        pygame.display.set_caption(c.SCREEN_NAME + ": " + message)
        pygame.display.set_icon(content.fetch().Sprite("icon"))

        self.clock = pygame.time.Clock()

        # my stuff
        self.circlePos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
        #deltatime
        self.deltaTime = 0
    def coreLoop(self):

        while self.running:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.circlePos.y -= 300 * self.deltaTime
            if keys[pygame.K_s]:
                self.circlePos.y += 300 * self.deltaTime
            if keys[pygame.K_a]:
                self.circlePos.x -= 300 * self.deltaTime
            if keys[pygame.K_d]:
                self.circlePos.x += 300 * self.deltaTime

            self.display.fill("purple")

            pygame.draw.circle(self.display, "red", self.circlePos, 40)

            self.window.blit(self.display, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
            pygame.display.flip()

            self.deltaTime = self.clock.tick(c.FRAME_RATE) / 1000

        pygame.quit()

    def close(self):

        l.Logger.log("Shutting Down")

        self.running = False
