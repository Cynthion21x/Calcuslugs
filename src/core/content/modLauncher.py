import os
import json
import pygame
import src.shared.constants as c
import src.shared.logger as l

class modLauncher:

    def __init__(self, content):

        self.modPath = c.DATA_PATH + "\\Mods"

        self.mods = dict()
        self.modPaths = []

        self.content = content

    def loadMods(self):

        # Find mods
        for i in os.listdir(self.modPath):

            if i == "Disabled":

                continue

            cDir = os.path.join(self.modPath, i)

            if os.path.isdir(cDir):

                f = None

                try:

                    f = open(cDir + "\\mod.json")
                    self.modPaths.append(cDir)

                except:

                    l.Logger.log("Could not find mod in directory", cDir, c.Logs.WARNING)

                    continue

                modDat = json.load(f)

                self.mods[i] = modDat

                l.Logger.log("Registered Mod", modDat["name"])

                f.close()

        # Load them in
                
        for x in self.modPaths:

            # Overrides first

            pathName = os.path.basename(x)

            if os.path.exists(x + "\\override"):

                # Text
                if os.path.exists(x + "\\override\\titleText.txt"):
                    self.content.textBase["title"] = x + "\\override\\titleText.txt"

                if (os.path.exists(x + "\\override\\language")):

                    cdir = x + "\\override\\language"

                    for i in os.listdir(cdir):

                        cF = cdir + "\\" + i

                        f = open(cF)

                        name = os.path.splitext(i)[0]

                        l.Logger.log("Loading", i)

                        try:

                            self.content.textBase[name] = json.load(f)

                        except:

                            l.Logger.log("Failed to load " + i + "in", self.mods[pathName]["name"], c.Logs.ERROR)

                        f.close()

                # Sprites
                
                if os.path.exists(x + "\\override\\icon.png"):
                    self.content.spriteBase["icon"] = pygame.image.load(x + "\\override\\icon.png")

                if (os.path.exists(x + "\\override\\picture")):

                    cdir = x + "\\override\\picture"

                    for i in os.listdir(cdir):

                        cF = cdir + "\\" + i

                        name = os.path.splitext(i)[0]

                        l.Logger.log("Loading", i)

                        try:

                            self.content.spriteBase[name] = pygame.image.load(cF)

                        except:

                            l.Logger.log("Failed to load " + i + "in", self.mods[pathName]["name"], c.Logs.WARNING)

            l.Logger.log("Loaded Mod", self.mods[pathName]["name"])