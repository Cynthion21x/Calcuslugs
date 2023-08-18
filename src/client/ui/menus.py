import pygame

import Game.src.client.ui.uielements as ui
import Game.src.shared.constants as c

class mainMenu():
    
    def __init__(self, game):

        self.game = game
        self.display = game.display

        self.background = ui.photo(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "\\sprites\\UI\\BG.png")

        self.HostButton = ui.button(186, 370, 240, 80, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "Host")
        self.JoinButton = ui.button(570, 370, 240, 80, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "Join")

        self.backButton = ui.button(570, 370, 100, 60, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "back")

        popUpshadow = ui.primativeElement(0, 0, 1040, 585, c.Colours.SHADOW, True)

        Menubg = ui.primativeElement(180, 96, 680, 389, c.Colours.GREY)

        self.joinMenu = ui.popupMenu([
            
            popUpshadow,
            Menubg,
            self.backButton
            
        ])

        self.hostMenu = ui.popupMenu([
            
            popUpshadow,
            Menubg,
            self.backButton
            
        ])

        self.hostMenu.disable()
        self.joinMenu.disable()

        def backButton():
            self.hostMenu.disable()
            self.joinMenu.disable()
            self.JoinButton.focused = True
            self.HostButton.focused = True


        def joinbutton():
            self.joinMenu.enable()
            self.JoinButton.focused = False
            self.HostButton.focused = False

        def hostbutton():
            self.hostMenu.enable()
            self.JoinButton.focused = False
            self.HostButton.focused = False

        self.JoinButton.appendAction(joinbutton)
        self.HostButton.appendAction(hostbutton)
        self.backButton.appendAction(backButton)

    def run(self):

        self.HostButton.process()
        self.JoinButton.process()
        self.backButton.process()

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