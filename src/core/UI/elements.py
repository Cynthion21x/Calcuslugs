import pygame

class UiElement:

    def __init__(self, pos, size):

        self.pos = pos
        self.size = size

class photo(UiElement):

    def __init__(self, pos, size, image):

        super().__init__(pos, size)

        self.image = image

    def render(self, display):

        display.blit(self.image, self.pos.value())