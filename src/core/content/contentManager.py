import os
import json
import src.shared.constants as c
import src.core.content.modLauncher as m

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



        self.modLauncher.loadMods()

    def getText(self, name):

        try:

            data = self.textBase[name]

        except:

            print("Resourse " + name + " failed to load")

            return -1
        
        return data

    def getSprite(self, name):

        pass

    def getSound(self, name):

        pass