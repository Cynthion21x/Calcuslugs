import pygame

class inputManager:

    def __init__(self):

        self.ENTER_KEY = False
        self.MOUSE_DOWN = False

    #TODO FIX MOUSE DOWN SO IT ONLY LASTS 1 FRAME

    def checkEvents(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False
                pygame.quit()

            # check inputs

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    self.ENTER_KEY = True

            mouse_buttons = pygame.mouse.get_pressed()

            if mouse_buttons[0] and not self.MOUSE_DOWN:
                self.MOUSE_DOWN = True
                print("Mouse left button clicked")

            if not mouse_buttons[0]:
                self.MOUSE_DOWN = False
    
    def resetInput(self):

        self.ENTER_KEY = False
        self.MOUSE_DOWN = False