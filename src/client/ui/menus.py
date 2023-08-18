import pygame

import Game.src.client.ui.uielements as ui
import Game.src.shared.constants as c

class mainMenu():
    
    def __init__(self, game):

        self.game = game
        self.display = game.display

        self.background = ui.photo(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "\\sprites\\UI\\BG.png")

        self.HostButton = ui.button(170, 370, 240, 80, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "Host")
        self.JoinButton = ui.button(570, 370, 240, 80, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "Join")

        popUpshadow = ui.primativeElement(0, 0, 1040, 585, c.Colours.SHADOW)

        self.joinMenu = ui.popupMenu([
            
            popUpshadow,
            
        ])

        self.hostMenu = ui.popupMenu([
            
            popUpshadow,
            
        ])

        self.hostMenu.disable()
        self.joinMenu.disable()

        self.JoinButton.appendAction(self.joinMenu.enable)
        self.HostButton.appendAction(self.hostMenu.enable)

    def run(self):

        self.HostButton.process()
        self.JoinButton.process()

        # >>>>>>>>>>>>>>>>>>>>>>>

        self.background.render(self.display)

        self.HostButton.render(self.display)
        self.JoinButton.render(self.display)

        self.hostMenu.run(self.display)
        self.joinMenu.run(self.display)

class lobby():
    
    def __init__(self, game):

        pass

class gameUi():
    
    def __init__(self, game):

        pass