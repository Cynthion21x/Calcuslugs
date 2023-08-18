import os
import pygame
import Game.src.shared.constants as c

pygame.font.init()

font = c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf"

class photo():

    def __init__(self, x, y, w, h, imagePath):

        self.x = x
        self.y = y

        self.photo = pygame.image.load(c.ASSETS_PATH + imagePath).convert()
        self.photo = pygame.transform.smoothscale(self.photo, (w, h))

        self.active = True

    def render(self, surface):

        surface.blit(self.photo, (self.x, self.y))

class primativeElement():

    def __init__(self, x, y, w, h, colour = c.Colours.WHITE, alpha=False):

        self.active = True
        self.alpha = alpha

        self.x = x
        self.y = y

        self.w = w
        self.h = h
        
        self.colour = colour

    def process(self):

        pass

    def render(self, surface):

        if self.alpha:

            s = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

            pygame.draw.rect(s, self.colour, (self.x, self.y, self.w, self.h))

            s.set_alpha(70)

            surface.blit(s, (0, 0))

        else:

            pygame.draw.rect(surface, self.colour, (self.x, self.y, self.w, self.h))
        

class label(primativeElement):

    def __init__(self, x, y, w, h, colour = c.Colours.INVISIBLE, textColour = c.Colours.BLACK, text='', fontSize = 32):

        self.active = True

        self.x = x
        self.y = y

        self.w = w
        self.h = h
        
        self.colour = colour

        self.text = text
        self.fontSize = fontSize
        self.textColour = textColour

    def render(self, surface):

        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.w, self.h))
        font = pygame.font.Font(c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf", self.fontSize)
        textSurf = font.render(self.text, False, self.textColour)

        textX = self.x + (self.w - textSurf.get_width()) // 2
        textY = self.y + (self.h - textSurf.get_height()) // 2

        surface.blit(textSurf, (textX, textY))
        

class inputBox(label):

    pass

class button(label):
    
    def __init__(self, inputManager, x, y, w, h, colour=c.Colours.WHITE, hoverColour=c.Colours.GREY, textColour=c.Colours.BLACK, text='', fontSize = 32, onClick=None):

        super().__init__(x, y, w, h, colour, textColour, text, fontSize)
        self.onClick = onClick
        self.hoverColour = hoverColour
        self.inputm = inputManager
        self.hovered = False
        self.focused = True
        self.active = True

    def process(self):

        mousePos = pygame.mouse.get_pos()
        clicked = self.inputm.MOUSE_DOWN

        if self.focused and self.active and self.x <= mousePos[0] <= self.x + self.w and self.y <= mousePos[1] <= self.y + self.h:

            self.hovered = True

            if clicked and self.onClick:

                self.onClick()

        else:

            self.hovered = False

    def appendAction(self, onClick=None):

        self.onClick = onClick

    def render(self, surface):

        if self.hovered:

            col = self.hoverColour

        else:

            col = self.colour

        pygame.draw.rect(surface, col, (self.x, self.y, self.w, self.h))
        
        font = pygame.font.Font(c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf", self.fontSize)
        textSurf = font.render(self.text, False, self.textColour)

        textX = self.x + (self.w - textSurf.get_width()) // 2
        textY = self.y + (self.h - textSurf.get_height()) // 2

        surface.blit(textSurf, (textX, textY))

class popupMenu():

    def __init__(self, primatves):

        self.primatves = primatves

    def run(self, surface):

        for primativeElement in self.primatves:

            if primativeElement.active == True:

                primativeElement.process()
                primativeElement.render(surface)

    def disable(self):

        for primativeElement in self.primatves:

            primativeElement.active = False
        
    def enable(self):

        for primativeElement in self.primatves:

            primativeElement.active = True