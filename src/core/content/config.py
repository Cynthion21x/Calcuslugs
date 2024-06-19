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

        if os.path.exists(self.optionFile) == False:

            self.file = open(self.logFile, 'a')
