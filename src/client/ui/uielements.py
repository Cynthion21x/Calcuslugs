import pygame
import pyperclip
import Game.src.shared.constants as c

pygame.font.init()

font = c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf"

class photo():

    def __init__(self, x, y, w, h, imagePath):

        self.x = x
        self.y = y

        self.photo = pygame.image.load(c.ASSETS_PATH + imagePath).convert_alpha()
        self.photo = pygame.transform.scale(self.photo, (w, h))

        self.active = True

    def render(self, surface):

        surface.blit(self.photo, (self.x, self.y))

    def process(self):

        pass

class photoButton(photo):

    def __init__(self, inputManager, x, y, w, h, fontsize, textColour, imagePath="\\images\\UI\\buttons\\standardButton", text="", action=None):

        super().__init__(x, y, w, h, imagePath + ".png")

        self.hoverphoto = pygame.image.load(c.ASSETS_PATH + imagePath + "-h.png").convert_alpha()
        self.hoverphoto = pygame.transform.smoothscale(self.hoverphoto, (w, h))

        self.inputm = inputManager
        self.hovered = False
        self.focused = True
        self.active = True

        self.onClick = action

        self.fontSize = fontsize

        self.text = text
        self.textColour = textColour

        self.w = w
        self.h = h

    def appendAction(self, onClick=None):

        self.onClick = onClick

    def render(self, surface):

        if (self.hovered):

            surface.blit(self.hoverphoto, (self.x, self.y))

        else:

            surface.blit(self.photo, (self.x, self.y))

        font = pygame.font.Font(c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf", self.fontSize)
        textSurf = font.render(self.text, True, self.textColour)

        textX = self.x + (self.w - textSurf.get_width()) // 2
        textY = self.y + (self.h - textSurf.get_height()) // 2

        surface.blit(textSurf, (textX, textY))

    def process(self):

        mousePos = pygame.mouse.get_pos()
        clicked = self.inputm.MOUSE_DOWN

        if self.focused and self.active and self.x <= mousePos[0] <= self.x + self.w and self.y <= mousePos[1] <= self.y + self.h:

            self.hovered = True

            if clicked and self.onClick:

                self.onClick()

        else:

            self.hovered = False

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

    def __init__(self, x, y, w, h, textColour = c.Colours.BLACK, text='', fontSize = 32):

        self.active = True

        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.text = text
        self.fontSize = fontSize
        self.textColour = textColour

    def render(self, surface):

        font = pygame.font.Font(c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf", self.fontSize)
        textSurf = font.render(self.text, True, self.textColour)

        textX = self.x + (self.w - textSurf.get_width()) // 2
        textY = self.y + (self.h - textSurf.get_height()) // 2

        surface.blit(textSurf, (textX, textY))
        

class inputBox(label):

    def __init__(self, inputManager, x, y, w, h, colour=c.Colours.WHITE, defaultTextColour=c.Colours.GREY, textColour=c.Colours.BLACK, defaultText='enterData', fontSize = 32):

        super().__init__(x, y, w, h, textColour, '', fontSize)

        self.colour = colour
        self.inputm = inputManager

        self.cursorPos = len(self.text)

        self.defaultTextColour = defaultTextColour
        self.textColour = textColour

        self.defautText = defaultText

        self.focused = True
        self.active = True
        self.Typing = False

    def process(self):
        
        mousePos = pygame.mouse.get_pos()
        clicked = self.inputm.MOUSE_DOWN

        if self.focused and self.active and self.x <= mousePos[0] <= self.x + self.w and self.y <= mousePos[1] <= self.y + self.h:

            #TODO change cursor type

            if clicked:

                self.Typing = True

        else:

            if clicked or self.active == False:

                self.Typing = False

        if self.Typing:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    # move mouse

                    if event.key == pygame.K_LEFT:
                        self.cursorPos = max(0, self.cursorPos - 1)
                    elif event.key == pygame.K_RIGHT:
                        self.cursorPos = min(len(self.text), self.cursorPos + 1)

                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        
                        self.text = self.text[:self.cursorPos] + pyperclip.paste() + self.text[self.cursorPos:]
                        self.cursorPos += len(pyperclip.paste())

                    # submit

                    elif event.key == self.inputm.ENTER_KEY:

                        print(self.text)

                    # typing
                    elif event.key == pygame.K_BACKSPACE:

                        self.text = self.text[:self.cursorPos - 1] + self.text[self.cursorPos:]
                        self.cursorPos -= 1

                    else:
                        
                        char = event.unicode
                        self.text = self.text[:self.cursorPos] + char + self.text[self.cursorPos:]
                        self.cursorPos += 1
                        self.cursorPos = max(0, min(self.cursorPos, len(self.text)))
    
    def render(self, surface):
        
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.w, self.h))

        font = pygame.font.Font(c.ASSETS_PATH + "\\fonts\cynthionStyle.ttf", self.fontSize)

        textToRender = self.text

        max_text_width = self.w - 90
        cursor_offset = 0

        text_start = max(0, self.cursorPos - max_text_width // font.size(' ')[0])
        text_end = min(text_start + max_text_width // font.size(' ')[0], len(self.text))

        if font.size(textToRender)[0] > max_text_width:
            cursor_offset = max(0, len(textToRender) - self.cursorPos - max_text_width // font.size(' ')[0])
            textToRender = textToRender[text_start:text_end]

        if self.text == '':

            textSurf = font.render(self.defautText, True, self.defaultTextColour)

        else:

            textSurf = font.render(textToRender, True, self.textColour)


        textX = self.x + (self.w - textSurf.get_width()) // 2
        textY = self.y + (self.h - textSurf.get_height()) // 2

        surface.blit(textSurf, (textX, textY))

        cursor_x = textX + font.size(self.text[:self.cursorPos - text_start])[0]
        if self.Typing and pygame.time.get_ticks() % 1000 < 500: 
            pygame.draw.line(surface, self.textColour, (cursor_x, textY), (cursor_x, textY + self.fontSize -2), 2)
                

class button(label):
    
    def __init__(self, inputManager, x, y, w, h, colour=c.Colours.WHITE, hoverColour=c.Colours.GREY, textColour=c.Colours.BLACK, text='', fontSize = 32, onClick=None):

        super().__init__(x, y, w, h, textColour, text, fontSize)
        self.colour = colour
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
        textSurf = font.render(self.text, True, self.textColour)

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