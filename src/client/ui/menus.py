import pygame
import Game.src.client.ui.uielements as ui
import Game.src.shared.constants as c

class mainMenu():
    
    def __init__(self, game):

        self.game = game
        self.display = game.display

        # >>>>>>>>>>>>>>>>>>>>>>

        self.background = ui.photo(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "\\images\\UI\\BG.png")
        self.title = ui.photo(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "\\images\\UI\\title.png")

        self.HostButton = ui.photoButton(game.inputManager, 186, 390, 240, 80, 32, c.Colours.WHITE, text="Host")
        self.JoinButton = ui.photoButton(game.inputManager, 570, 390, 240, 80, 32, c.Colours.WHITE, text="Join")

        enterIP = ui.label(330, 260+30, 1, 1, c.Colours.WHITE, "Enter IP", 30)

        ipTextBox = ui.inputBox(game.inputManager, 410, 247+30, 317, 32, c.Colours.WHITE, c.Colours.GREY, c.Colours.BLACK, 'Enter IP...', 30)

        enterPort = ui.label(330, 260+30, 1, 1, c.Colours.WHITE, "Enter Port", 30)

        PortTextBox = ui.inputBox(game.inputManager, 410, 247+30, 317, 32, c.Colours.WHITE, c.Colours.GREY, c.Colours.BLACK, '1700', 30)


        self.backButton = ui.button(game.inputManager, 640, 380, 100, 60, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "back")

        self.host = ui.button(game.inputManager, 280, 380, 100, 60, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "Host")
        self.join = ui.button(game.inputManager, 280, 380, 100, 60, c.Colours.BUTTON_NORMAL, c.Colours.BUTTON_HOVER, c.Colours.WHITE, "Join")

        popUpshadow1 = ui.primativeElement(0, 0, 1040, 585, c.Colours.SHADOW, True)
        popUpshadow2 = ui.primativeElement(0, 0, 1040, 585, c.Colours.SHADOW, True)
        


        CMenubg = ui.photo(180, 96, 680, 389, "\\images\\UI\\popup.png")
        JMenubg = ui.photo(180, 96, 680, 389, "\\images\\UI\\popup.png")

        createLabel = ui.label(0, 10, 1040, 300, c.Colours.WHITE, "Create a Game", 50)
        JoinLabel = ui.label(0, 10, 1040, 300, c.Colours.WHITE, "Join a Game", 50)

        # >>>>>>>>>>>>>>>>>>>>>>

        self.joinMenu = ui.popupMenu([
            
            popUpshadow1,
            JMenubg,
            self.backButton,
            JoinLabel,
            enterIP,
            ipTextBox,
            self.join
            
        ])

        self.hostMenu = ui.popupMenu([
            
            popUpshadow2,
            CMenubg,
            self.backButton,
            createLabel,
            enterPort,
            PortTextBox,
            self.host
            
        ])

        self.hostMenu.disable()
        self.joinMenu.disable()

        # >>>>>>>>>>>>>>>>>>>>>>

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

        def joinG():
            game.Join(ipTextBox.text)
            self.host.focused = False

        def hostG():
            game.Host(PortTextBox.text)
            self.host.focused = False

        self.JoinButton.appendAction(joinbutton)
        self.HostButton.appendAction(hostbutton)
        self.backButton.appendAction(backButton)

        self.join.appendAction(joinG)
        self.host.appendAction(hostG)

    def run(self):

        self.HostButton.process()
        self.JoinButton.process()
        self.backButton.process()

        # >>>>>>>>>>>>>>>>>>>>>>>

        self.background.render(self.display)
        self.title.render(self.display)

        self.HostButton.render(self.display)
        self.JoinButton.render(self.display)

        self.hostMenu.run(self.display)
        self.joinMenu.run(self.display)

class lobby():
    
    def __init__(self, game):

        self.display = game.display

        self.timer = 0

        self.bg = ui.photo(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "\\images\\UI\\Lobby.png")

        self.loading = ui.label(0, 0, 1040, 585, c.Colours.WHITE, "Waiting For Friends...", 32)

        self.main = ui.popupMenu([

            self.bg,
            self.loading

        ])

    def run(self, deltaTime):

        self.main.run(self.display)

        if self.timer >= 1:

            if (self.loading.text == "Waiting For Friends..."):
                
                self.loading.text = "Waiting For Friends"

            else:

                self.loading.text += "."

            self.timer = 0

        self.timer += deltaTime / 1000

class gameUi():
    
    def __init__(self, game):

        pass

    def run(self):

        pass