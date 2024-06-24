import os
import json
import pygame
import src.shared.constants as c
import src.core.content.modLauncher as m
import src.shared.logger as l

class Content:

    def __init__(self):

        if not os.path.isdir(c.DATA_PATH):

            os.mkdir(c.DATA_PATH)
            os.mkdir(c.DATA_PATH + "\\Mods")
            os.mkdir(c.DATA_PATH + "\\Settings")

        self.modLauncher = m.modLauncher(self)

        self.loadContent()

    def loadText(self):

        self.textBase["title"] = c.ASSETS_PATH + "\\titleText.txt"

        for i in os.listdir(c.ASSETS_PATH + "\\language"):

            cDir = c.ASSETS_PATH + "\\language\\" + i

            with open(cDir) as f:

                identifier = os.path.splitext(i)[0]

                l.Logger.log("Loading", i)

                try:

                    self.textBase[identifier] = json.load(f)

                except:

                    l.Logger.log("Failed to load", i, c.Logs.ERROR)

    def loadSprites(self):

        try:
            self.spriteBase["icon"] = pygame.image.load(c.ASSETS_PATH + "\\icon.png")
        except:
            l.Logger.log("Failed to load icon")

        for root, dirs, files in os.walk(c.ASSETS_PATH + "\\picture"):
            
            for file in files:

                cDir = root + "\\" + file

                identifier = root + "\\" + os.path.splitext(file)[0]

                identifier = identifier.replace(c.ASSETS_PATH + "\\picture\\", "")

                ending = os.path.splitext(file)[1]

                if (ending == ".png"):

                    l.Logger.log("Loading", identifier + ending)

                    try:

                        self.spriteBase[identifier] = pygame.image.load(cDir)

                    except:

                        l.Logger.log("Failed to load", file, c.Logs.WARNING)

    def loadFonts(self):

        pygame.font.init()

        for root, dirs, files in os.walk(c.ASSETS_PATH + "\\fonts"):
                    
            for file in files:

                cDir = root + "\\" + file

                identifier = root + "\\" + os.path.splitext(file)[0]

                identifier = identifier.replace(c.ASSETS_PATH + "\\fonts\\", "")

                l.Logger.log("Loading", identifier + os.path.splitext(file)[1])

                try:

                    self.fontBase[identifier] = pygame.font.Font(cDir, 64)

                except:

                    l.Logger.log("Failed to load", file, c.Logs.WARNING)   

    def loadContent(self):

        self.textBase = dict()

        self.spriteBase = dict()

        self.fontBase = dict()

        self.soundBase = dict()

        l.Logger.log("Loading Content...")

        self.loadText()

        self.loadSprites()

        self.loadFonts()

        self.modLauncher.loadMods()

        l.Logger.log("Content loaded!")
            


data = Content()

def fetch():

    if data is None:

        l.Logger.log("Don't acess data beffore its loaded", c.Logs.WARNING)

    return data

def Text(name):

    try:

        data = fetch().textBase[name]

        return data

    except:

        l.Logger.log("Failed to find text", name, c.Logs.ERROR)

        return c.Logs.ERROR

def Sprite(name):

    try:

        data = fetch().spriteBase[name]

    except:

        l.Logger.log("Failed to find sprite", name, c.Logs.WARNING)

        data = fetch().spriteBase["error"]

    return data

def Font(name):

    try:

        data = fetch().fontBase[name]

    except:

        l.Logger.log("Failed to find font", name, c.Logs.WARNING)

        data = fetch().fontBase["default"]

    return data  

def Sound(name):

    pass