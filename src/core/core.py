import pygame
import src.core.content.contentManager as content
from src.scenes import splashScreen, mainMenu, options, game, victory
import src.shared.constants as c
import src.shared.logger as l
import src.core.Input.inputManager as Input
import src.core.UI.elements as elements
import src.math.vectors as v
import src.core.content.config as config

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
        self.splashScreen = splashScreen.splashScreen(self)
        self.game = game.game(self)
        self.menu = mainMenu.mainMenu(self)
        self.victory = victory.victory(self)

        self.optionsMenu = options.options(self)
        self.showOptions = False

        self.prevState = self.GameState

        # Window

        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.DOUBLEBUF)

        pygame.display.set_caption(c.SCREEN_NAME + ": " + message)
        pygame.display.set_icon(content.Sprite("icon"))

        self.fpsCounter = elements.text(

            v.Vector(10, 10),
            v.Vector(20, 10), "60",
            content.Font("default")

        )

        c.FRAME_RATE = config.getOption("targetFPS")
        c.TILE_SIZE = config.getOption("pixelSize")
        c.GAME_WIDTH = int(c.GAME_WIDTH_REAL / c.TILE_SIZE)
        c.GAME_HEIGHT = int(c.GAME_HEIGHT_REAL / c.TILE_SIZE)

    def coreLoop(self):

        counter = 0
        total = 0

        while self.running:

            counter += 1

            # clear prev frame
            self.display.fill(c.Colours.BLACK)

            # Get Events
            Input.fetch().gatherInput()

            # Check state change

            if self.prevState != self.GameState:

                self.prevState = self.GameState
                l.Logger.log("Changed game state")

            # Run appropriate section of code

            if self.GameState == c.States.SPLASH:

                self.splashScreen.run()

            elif self.GameState == c.States.MENU:

                self.menu.run()

            elif self.GameState == c.States.GAME:

                self.game.run()

            elif self.GameState == c.States.VICTORY:

                self.victory.run()

            if self.showOptions:

                self.optionsMenu.run()

            if config.getOption("showFPS"):
                self.fpsCounter.render(self.display)

            # Update Display

            self.window.blit(self.display, (0, 0))
            
            pygame.display.flip()

            self.deltaTime = self.clock.tick(c.FRAME_RATE) / 1000

            total += self.clock.get_fps()

            if counter > config.getOption("fpsUpdateTime")-1:
                self.fpsCounter.updateText(str(int(total / counter)))
                counter = 0
                total = 0

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
