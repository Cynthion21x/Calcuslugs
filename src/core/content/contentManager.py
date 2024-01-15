import os
import json
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

        # text
        self.textBase["title"] = c.ASSETS_PATH + "\\titleText.txt"

        for i in os.listdir(c.ASSETS_PATH + "\\language"):

            cDir = c.ASSETS_PATH + "\\language\\" + i

            f = open(cDir)

            identifier = os.path.splitext(i)[0]

            self.textBase[identifier] = json.load(f)

            f.close()

        # Sprites

        self.modLauncher.loadMods()

    def getText(self, name):

        try:

            data = self.textBase[name]

        except:

            l.Logger.log("Resourse failed to load", name, c.Logs.ERROR)

            return -1
        
        return data

    def getSprite(self, name):

        pass

    def getSound(self, name):

        pass