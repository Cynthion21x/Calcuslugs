import pygame
import src.math.vectors as v
import src.shared.constants as c

class UiElement:

    def __init__(self, pos, size):

        self.pos = pos
        self.size = size

class text(UiElement):

    def __init__(self, pos, size, text, font=None, colour=c.Colours.WHITE):

        super().__init__(pos, size)

        self.textImg = font.render(text, True, colour)

        ratio = self.textImg.get_size()[1] / self.textImg.get_size()[0]

        newSize = v.Vector(size.x, size.x * ratio)

        self.textImg = pygame.transform.smoothscale(self.textImg, newSize.value())

    def render(self, display):

        display.blit(self.textImg, self.pos.value())

class photo(UiElement):

    def __init__(self, pos, size, image, preserveAspect = False):

        super().__init__(pos, size)

        if preserveAspect == False:

            self.image = pygame.transform.smoothscale(image, size.value())

        else:

            ratio = image.get_size()[1] / image.get_size()[0]

            newSize = v.Vector(size.x, size.x * ratio)

            self.image = pygame.transform.smoothscale(image, newSize.value())

    def render(self, display):

        display.blit(self.image, self.pos.value())