import os
import src.shared.constants as c

class logger:

    def __init__(self, path):
        
        if os.path.isdir(c.DATA_PATH) == False:

            os.mkdir(c.DATA_PATH)
            os.mkdir(c.DATA_PATH + "\\Mods")
            os.mkdir(c.DATA_PATH + "\\Settings")
        
        self.path = path
        self.logFile = path + "\\logs.txt"

        if os.path.exists(self.logFile):

            if os.path.exists(path + "\\logs-old.txt"):

                os.remove(path + "\\logs-old.txt")
            
            os.rename(self.logFile, path + "\\logs-old.txt")

        self.file = open(self.logFile, 'a')

        self.file.write("---- THESE ARE THE LOGS BUCKO ----" + "\n")

        self.log("Welcome to calcuslugs :)")

    def log(self, message, details = None, logLevel = c.Logs.NORMAL):

        if details:

            text = message + ": " + str(details)

        else: 

            text = message

        if logLevel == c.Logs.WARNING:

            text = "WARNING: " + text

        elif logLevel == c.Logs.ERROR:

            text = "ERROR: " + text

        print(text)

        self.file.write(text + "\n")

    def close(self):
        
        self.file.close()


Logger = logger(c.DATA_PATH)