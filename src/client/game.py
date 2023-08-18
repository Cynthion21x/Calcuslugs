import pygame
import Game.src.shared.constants as c
import Game.src.client.ui.menus as ui
import Game.src.client.inputManager as inputman

class Game():

    def __init__(self, message):

        pygame.init()

        self.message = message

        # >>>>>>>>>>>>>>>>>>>>>
        
        self.running = True
        self.state = c.States.MAIN_MENU

        # >>>>>>>>>>>>>>>>>>>>>

        self.inputManager = inputman.inputManager()

        # >>>>>>>>>>>>>>>>>>>>>


        self.display = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        
        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption(c.SCREEN_NAME + ": " + message)
        pygame.display.set_icon(pygame.image.load(c.ASSETS_PATH + "\icon.png"))

        self.clock = pygame.time.Clock()

        # >>>>>>>>>>>>>>>>>>>>>

        self.mainMenu = ui.mainMenu(self)
        self.lobby = ui.lobby(self)
        self.gameUi = ui.gameUi(self)

    def coreLoop(self):

        while self.running:

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # first pass

            self.inputManager.checkEvents()

            self.display.fill(c.Colours.NUCLEAR_SNOT_GREEN)

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # game pass

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # ui pass

            if self.state == c.States.MAIN_MENU:

                self.mainMenu.run()

            elif self.state == c.States.LOBBY:

                self.lobby.run()

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            # final pass

            self.window.blit(self.display, (0, 0))

            pygame.display.update()

            self.inputManager.resetInput()

            self.clock.tick(c.FRAME_RATE)   
