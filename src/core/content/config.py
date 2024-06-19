import os
import json
import pygame
import src.shared.constants as c
import src.shared.logger as l

class Options:

    def __init__(self):

        self.optionFile = c.DATA_PATH + "\\Settings\\options.json"

        self.ops = dict()

        self.loadContent()

        if not os.path.exists(self.optionFile):

            l.logger.Log("Options not found, writing default options", )

            self.file = open(self.logFile, 'x')
            
            with open(c.ASSETS_PATH, "defaultOptions.json") as default:

                self.file.write(default.read())

        else:

            self.file = open(self.logFile, 'r')

        self.ops = json.load(self.file)


options = Options()

def getOption(name):

    # handling for missing options at some point in the future

    return options.ops[name]
