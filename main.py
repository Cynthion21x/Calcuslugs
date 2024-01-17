import src.core.game as g
import src.core.content.contentManager as content
import src.shared.logger as l

import random

lines = open(content.fetch().Text("title")).read().splitlines()
selection = random.choice(lines)

# Main Loop

main = g.Game(selection)

main.coreLoop()

l.Logger.log("Goodbye World")