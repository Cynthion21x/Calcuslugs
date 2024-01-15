import os
import json
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

                        self.content.textBase[name] = json.load(f)

                        f.close()

            l.Logger.log("Loaded Mod", self.mods[pathName]["name"])