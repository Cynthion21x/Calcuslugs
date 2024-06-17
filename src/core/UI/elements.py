import pygame
import src.math.vectors as v
import src.shared.constants as c
import src.core.Input.inputManager as Input

class UiElement:

    def __init__(self, pos, size):

        self.pos = pos
        self.size = size


class button(UiElement):

    def __init__(self, pos, size, function, display, displayHover):

        super().__init__(pos, size)

        self.function = function
        self.hovered = False

        self.activeDisplay = display

        self.default = display
        self.hover = displayHover

    def run(self):

        boundL = self.pos
        boundU = v.add(self.pos, self.size)

        mouse = Input.fetch().getMousePos()

        if (boundL.x < mouse.x < boundU.x) and ((boundL.y < mouse.y < boundU.y)):

            self.activeDisplay = self.hover

            if (Input.fetch().MOUSE_UP):

                self.function()

        else:

            self.activeDisplay = self.default

    def render(self, display):

        self.activeDisplay.render(display)

class text(UiElement):

    def __init__(self, pos, size, text, font=None, colour=c.Colours.WHITE):

        super().__init__(pos, size)

        self.textImg = font.render(text, True, colour)

        ratio = self.textImg.get_size()[1] / self.textImg.get_size()[0]

        newSize = v.Vector(size.x, size.x * ratio)

        self.textImg = pygame.transform.smoothscale(self.textImg, newSize.value())

    def render(self, display):

        display.blit(self.textImg, self.pos.value())

    def run(self, inputM):
        
        pass

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

    def run(self):
        
        pass

class group:

    def __init__(self, elements):

        self.visible = True
        self.interactive = True

        self.elements = elements

    def run(self, display):

        for i in self.elements:

            if self.interactive:

                i.run()

            if self.visible:

                i.render(display)

class inputBox(UiElement):

    pass