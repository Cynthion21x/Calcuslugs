import os
import json
import pygame
import src.shared.constants as c
import src.core.content.modLauncher as m
import src.shared.logger as l

class Content:

    def __init__(self):

        if os.path.isdir(c.DATA_PATH) == False:

            os.mkdir(c.DATA_PATH)
            os.mkdir(c.DATA_PATH + "\\Mods")
            os.mkdir(c.DATA_PATH + "\\Settings")

        self.modLauncher = m.modLauncher(self)

        self.loadContent()

    def loadContent(self):

        self.textBase = dict()

        self.spriteBase = dict()

        self.soundBase = dict()

        l.Logger.log("Loading Content...")

        # text
        self.textBase["title"] = c.ASSETS_PATH + "\\titleText.txt"

        for i in os.listdir(c.ASSETS_PATH + "\\language"):

            cDir = c.ASSETS_PATH + "\\language\\" + i

            f = open(cDir)

            identifier = os.path.splitext(i)[0]

            l.Logger.log("Loading", i)

            try:

                self.textBase[identifier] = json.load(f)

            except:

                l.Logger.log("Failed to load", i, c.Logs.ERROR)

            f.close()

        # Sprites

        self.spriteBase["icon"] = pygame.image.load(c.ASSETS_PATH + "\\icon.png")

        for i in os.listdir(c.ASSETS_PATH + "\\picture"):

            cDir = c.ASSETS_PATH + "\\picture\\" + i

            identifier = os.path.splitext(i)[0]

            l.Logger.log("Loading", i)

            try:

                self.spriteBase[identifier] = pygame.image.load(cDir)

            except:

                l.Logger.log("Failed to load", i, c.Logs.WARNING)

        self.modLauncher.loadMods()

        l.Logger.log("Content loaded!")

    def Text(self, name):

        try:

            data = self.textBase[name]

            return data

        except:

            l.Logger.log("Text failed to load", name, c.Logs.ERROR)

            return c.Logs.ERROR

    def Sprite(self, name):

        try:

            data = self.spriteBase[name]

            return data

        except:

            l.logger.log("Image failed to load", name, c.Logs.ERROR)

            return c.Logs.ERROR

    def getSound(self, name):

        pass

data = Content()

def fetch():

    if data == None:

        l.Logger.log("Don't acess data beffore its loaded", c.Logs.WARNING)

    return data