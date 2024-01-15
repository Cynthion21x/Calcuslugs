import src.core.game as g
import src.core.content.contentManager as content
import src.shared.logger as l

import random

# Load Content

loader = content.Content()

lines = open(loader.getText("title")).read().splitlines()
selection = random.choice(lines)

# Main Loop

main = g.Game(selection)

main.coreLoop()

l.Logger.log("Goodbye World")