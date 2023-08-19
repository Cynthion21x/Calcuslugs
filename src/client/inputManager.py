import sys
import pygame

class inputManager:

    def __init__(self):

        self.ENTER_KEY = False
        self.MOUSE_DOWN = False
        self.MOUSE_HOLD = False

    #TODO FIX MOUSE DOWN SO IT ONLY LASTS 1 FRAME

    def checkEvents(self):

        pygame.event.pump()

        mouseButtons = pygame.mouse.get_pressed()

        if mouseButtons[0]:

            if self.MOUSE_HOLD == False:

                self.MOUSE_DOWN = True
                self.MOUSE_HOLD = True

            else:
                
                self.MOUSE_DOWN = False

        else:

            self.MOUSE_HOLD = False


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False
                pygame.quit()
                sys.exit(0)

            # check inputs

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    self.ENTER_KEY = True
    
    def resetInput(self):

        self.ENTER_KEY = False
        self.MOUSE_DOWN = False