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

        self.textBase["title"] = os.path.join(c.ASSETS_PATH, "titleText.txt")

        for i in os.listdir(os.path.join(c.ASSETS_PATH, "language")):

            cDir = os.path.join(c.ASSETS_PATH, "language", i)

            with open(cDir) as f:

                identifier = os.path.splitext(i)[0]

                l.Logger.log("Loading", i)

                try:

                    self.textBase[identifier] = json.load(f)

                except:

                    l.Logger.log("Failed to load", i, c.Logs.ERROR)

    def loadSprites(self):

        try:
            self.spriteBase["icon"] = pygame.image.load(os.path.join(c.ASSETS_PATH, "icon.png")).convert_alpha()
        except:
            l.Logger.log("Failed to load icon")

        for root, dirs, files in os.walk(os.path.join(c.ASSETS_PATH, "picture")):
            
            for file in files:

                cDir = os.path.join(root, file)

                identifier = root + "/" +  os.path.splitext(file)[0]

                identifier = identifier.replace(os.path.join(c.ASSETS_PATH, "picture", ""), "")

                ending = os.path.splitext(file)[1]

                if (ending == ".png"):

                    l.Logger.log("Loading", identifier + ending)

                    try:

                        self.spriteBase[identifier] = pygame.image.load(cDir)

                    except:

                        l.Logger.log("Failed to load", file, c.Logs.WARNING)

    def loadFonts(self):

        pygame.font.init()

        for root, dirs, files in os.walk(os.path.join(c.ASSETS_PATH, "fonts")):
                    
            for file in files:

                cDir = os.path.join(root, file)

                identifier = root + "/" +  os.path.splitext(file)[0]

                identifier = identifier.replace(os.path.join(c.ASSETS_PATH, "fonts", ""), "")

                l.Logger.log("Loading", identifier + os.path.splitext(file)[1])

                try:

                    self.fontBase[identifier] = pygame.font.Font(cDir, 64)

                except:

                    l.Logger.log("Failed to load", file, c.Logs.WARNING)   

    def loadGuns(self):

        l.Logger.log("Loading Guns...")

        for i in os.listdir(os.path.join(c.ASSETS_PATH, "guns")):

            cDir = os.path.join(c.ASSETS_PATH, "guns", i)

            with open(cDir) as f:

                identifier = os.path.splitext(i)[0]

                l.Logger.log("Loading", i)

                try:

                    self.gunBase[identifier] = json.load(f)

                except Exception as e:

                    l.Logger.log("Failed to load", i, c.Logs.ERROR)  
                    l.Logger.log(e, logLevel=c.Logs.ERROR)

    def loadSlugs(self):

        l.Logger.log("Loading Slugs...")

        for i in os.listdir(os.path.join(c.ASSETS_PATH, "slugs")):

            cDir = os.path.join(c.ASSETS_PATH, "slugs", i)

            with open(cDir) as f:

                identifier = os.path.splitext(i)[0]

                l.Logger.log("Loading", i)

                try:

                    self.slugBase[identifier] = json.load(f)

                except:

                    l.Logger.log("Failed to load", i, c.Logs.ERROR)     

    def loadContent(self):

        self.textBase = dict()

        self.spriteBase = dict()

        self.fontBase = dict()

        self.soundBase = dict()

        self.gunBase = dict()

        self.slugBase = dict()

        l.Logger.log("Loading Content...")

        # Assets
        self.loadText()

        self.loadSprites()

        self.loadFonts()

        # Recourses
        self.loadGuns()
        self.loadSlugs()

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

def Slug(name):

    try:

        data = fetch().slugBase[name]
        return data

    except:

        l.Logger.log("Failed to find slug", name, c.Logs.ERROR)

def Gun(name):

    try:

        data = fetch().gunBase[name]
        return data

    except:

        l.Logger.log("Failed to find gun", name, c.Logs.ERROR)
 

def Sound(name):

    pass