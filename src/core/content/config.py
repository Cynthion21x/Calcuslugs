import os
import json

import json.scanner
import src.shared.constants as c
import src.shared.logger as l

class Options:

    def __init__(self):

        self.optionFile = c.DATA_PATH + "\\Settings\\options.json"

        defaultOptions = c.ASSETS_PATH + "\\defaultOptions.json"

        l.Logger.log("Loading Default Options")
        
        with open(defaultOptions, 'r') as file:

            self.defaultOps = json.load(file)

        l.Logger.log("Loaded Default Options")

        self.ops = dict()

        l.Logger.log("Loading user options")

        if not os.path.exists(self.optionFile):

            l.Logger.log("Options not found, writing default options...")

            self.file = open(self.optionFile, 'x')
            
            with open(defaultOptions) as default:

                self.file.write(default.read())

            l.Logger.log("Options written!")

        else:

            with open(self.optionFile, 'r') as file:

                self.ops = json.load(file)

        l.Logger.log("Options loaded!")


options = Options()

def getOption(name):

    # handling for missing options at some point in the future
    # The future is now

    if not (name in options.ops.keys()):

        if not (name in options.defaultOps.keys()):

            l.Logger.log("Could not find option", name, c.Logs.ERROR)

        else:

            l.Logger.log("could not find option in current options file", name, c.Logs.WARNING)

            options.ops[name] = options.defaultOps[name]

            l.Logger.log("Adding option to file...")

            with open(options.optionFile, 'w') as file:

                file.write(json.dumps(options.ops, indent=4))

                l.Logger.log("Added Option to file!")

            return options.defaultOps[name]

    else:

        return options.ops[name]
