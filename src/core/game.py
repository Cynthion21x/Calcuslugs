import pygame
import src.core.inputManager as inputManager
import src.shared.constants as c

class Game():

    def __init__(self, message):

        pygame.init()

        self.message = message

        self.running = True

        self.display = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        pygame.display.set_caption(c.SCREEN_NAME + ": " + message)
        pygame.display.set_icon(pygame.image.load(c.ASSETS_PATH + "\\icon.png"))

        self.clock = pygame.time.Clock()


    def coreLoop(self):

        while self.running:

            self.window.blit(self.display, (0, 0))

            pygame.display.update()

            self.deltaTime = self.clock.tick(c.FRAME_RATE)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.close()

        pygame.quit()

    def close(self):

        print("Stopping game")

        self.running = False