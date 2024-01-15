import os
import src.shared.constants as c

class logger:

    def __init__(self, path):

        self.path = path
        self.logFile = path + "\\logs.txt"

        if os.path.exists(self.logFile):

            if os.path.exists(path + "\\logs-old.txt"):

                os.remove(path + "\\logs-old.txt")
            
            os.rename(self.logFile, path + "\\logs-old.txt")

        self.file = open(self.logFile, 'a')

        self.log("So you had a problemo huh... well this is where you see what happened buckeo")

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