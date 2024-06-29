import pygame
import src.core.content.contentManager as content
import src.scenes.splashScreen as splash
import src.scenes.game as game
import src.scenes.mainMenu as menu
import src.shared.constants as c
import src.shared.logger as l
import src.core.Input.inputManager as Input

class Game():

    def __init__(self, message):

        self.closing = False

        self.GameState = c.States.SPLASH

        self.message = message

        self.running = True

        self.display = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        # my stuff
        self.circlePos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)

        #vdeltatime
        self.deltaTime = 0

        # scenes
        self.splashScreen = splash.splashScreen(self)
        self.game = game.game(self)
        self.menu = menu.mainMenu(self)

        self.prevState = self.GameState

        # Window

        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        pygame.display.set_caption(c.SCREEN_NAME + ": " + message)
        pygame.display.set_icon(content.Sprite("icon"))

    def coreLoop(self):

        while self.running:

            # clear prev frame
            self.display.fill(c.Colours.BLACK)

            # Get Events
            Input.fetch().gatherInput()

            # Check state change

            if self.prevState != self.GameState:

                self.prevState = self.GameState
                l.Logger.log("Changed game state")

                # subscribable event here or something

            # Run appropriate section of code

            if self.GameState == c.States.SPLASH:

                self.splashScreen.run()

            elif self.GameState == c.States.MENU:

                self.menu.run()

            elif self.GameState == c.States.GAME:

                self.game.run()

            # Update Display

            self.window.blit(self.display, (0, 0))
            pygame.display.flip()

            self.deltaTime = self.clock.tick(c.FRAME_RATE) / 1000

            # Exit
            if Input.fetch().QUIT:
                self.exit()

            if self.closing:

                self.close()

    def close(self):

        l.Logger.log("Shutting Down")
        l.Logger.close()
        pygame.quit()
        self.running = False

    def exit(self):

        self.closing = True
