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

                    f = open(os.path.join(cDir, "mod.json"))
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

            if os.path.exists(os.path.join(x, "override")):

                # Text
                if os.path.exists(os.path.join(x, "override", "titleText.txt")):
                    self.content.textBase["title"] = os.path.join(x, "override", "titleText.txt")

                if (os.path.exists(os.path.join(x, "override", "language"))):

                    cdir = os.path.join(x, "override", "language")

                    for i in os.listdir(cdir):

                        cF = os.path.join(cdir, i)

                        with open(cF) as f:

                            name = os.path.splitext(i)[0]

                            l.Logger.log("Loading", i)

                            try:

                                self.content.textBase[name] = json.load(f)

                            except:

                                l.Logger.log("Failed to load " + i + "in", self.mods[pathName]["name"], c.Logs.ERROR)


                # Sprites
                
                if os.path.exists(os.path.join(x, "override", "icon.png")):
                    
                    self.content.spriteBase["icon"] = pygame.image.load(os.path.join(x, "override", "icon.png"))

                if (os.path.exists(os.path.join(x, "override", "picture"))):

                    cdir = os.path.join(x, "override", "picture")

                    for root, dirs, files in os.walk(cdir):

                        for file in files:

                            cF = os.path.join(root, file)

                            identifier = os.path.join(root, os.path.splitext(file)[0])

                            identifier = identifier.replace(os.path.join(cdir, ""), "")

                            l.Logger.log("Loading", identifier + os.path.splitext(file)[1])

                            try:

                                self.content.spriteBase[identifier] = pygame.image.load(cF)

                            except:

                                l.Logger.log("Failed to load " + identifier + "in", self.mods[pathName]["name"], c.Logs.WARNING)

            l.Logger.log("Loaded Mod", self.mods[pathName]["name"])