import os
import src.shared.constants as c
import json

class modLauncher:

    def __init__(self, content):

        self.modPath = c.DATA_PATH + "\\Mods"

        self.mods = []

        self.content = content

    def loadMods(self):

        for i in os.listdir(self.modPath):

            cDir = os.path.join(self.modPath, i)

            if os.path.isdir(cDir):

                f = None

                try:

                    f = open(cDir + "\\mod.json")

                except:

                    print("Could not find mod in " + cDir)

                    continue

                modDat = json.load(f)

                self.mods.append(modDat)

                print("Loading Mod: " + modDat["name"])