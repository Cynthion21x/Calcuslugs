import src.math.vectors as v
import src.shared.constants as c
import src.core.Input.inputManager as Input
import src.shared.logger as l
import pygame
import time
import math

def create_gaussian_kernel(radius, sigma):
    kernel = [0] * (2 * radius + 1)
    sum_val = 0.0

    for i in range(-radius, radius + 1):
        kernel[i + radius] = (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(- (i ** 2) / (2 * sigma ** 2))
        sum_val += kernel[i + radius]

    # Normalize the kernel
    for i in range(len(kernel)):
        kernel[i] /= sum_val

    return kernel

def blur(surface, radius):

    l.Logger.log("Starting Blur algorithm")

    start = time.process_time()

    width, height = surface.get_size()
    pixels = pygame.PixelArray(surface)
    blurred_surface = pygame.Surface((width, height))
    kernel = create_gaussian_kernel(radius, radius / 3)

    # Horizontal pass
    for y in range(height):
        for x in range(width):
            r, g, b = 0, 0, 0
            for k in range(-radius, radius + 1):
                px = min(width - 1, max(0, x + k))
                color = surface.get_at((px, y))
                kernel_val = kernel[k + radius]
                r += color.r * kernel_val
                g += color.g * kernel_val
                b += color.b * kernel_val
            blurred_surface.set_at((x, y), (int(r), int(g), int(b)))

    # Vertical pass
    final_surface = pygame.Surface((width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = 0, 0, 0
            for k in range(-radius, radius + 1):
                py = min(height - 1, max(0, y + k))
                color = blurred_surface.get_at((x, py))
                kernel_val = kernel[k + radius]
                r += color.r * kernel_val
                g += color.g * kernel_val
                b += color.b * kernel_val
            final_surface.set_at((x, y), (int(r), int(g), int(b)))

    l.Logger.log("Image blurred", str(math.floor((time.process_time() - start) * 100) / 100) + "s")

    return final_surface

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

        self.updateCount = 0
        self.renderCount = 0

        self.font = font

        self.textImg = font.render(text, True, colour)

        self.colour = colour

        self.sizeIntented = size

        ratio = self.textImg.get_size()[1] / self.textImg.get_size()[0]

        self.newSize = v.Vector(size.x, size.x * ratio)

        self.textImg = pygame.transform.smoothscale(self.textImg, self.newSize.value())
        self.textImg.convert_alpha()

    def updateText(self, text):

        self.textImg = self.font.render(text, True, self.colour)

        ratio = self.textImg.get_size()[1] / self.textImg.get_size()[0]

        self.newSize = v.Vector(self.sizeIntented.x, self.sizeIntented.x * ratio)

        self.textImg = pygame.transform.smoothscale(self.textImg, self.newSize.value())

        if self.updateCount < self.renderCount:
            self.textImg.convert_alpha()

        self.updateCount += 1


    def render(self, display):

        display.blit(self.textImg, self.pos.value())

        self.renderCount += 1

    def run(self):
        
        pass

class textBox(UiElement):

    def __init__(self, pos, size, text, font=None, colour=c.Colours.BLACK, backgroundColor=c.Colours.WHITE):

        super().__init__(pos, size)

        self.font = font

        self.textImg = font.render(text, True, colour)

        self.colour = colour
        self.backgroundColour = backgroundColor

    def render(self, display):

        pygame.draw.rect(display, self.pos.value(), self.size.value())

    def run(self):
        
        pass

class photo(UiElement):

    def __init__(self, pos, size, image, preserveAspect = False):

        super().__init__(pos, size)

        if preserveAspect is False:

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
