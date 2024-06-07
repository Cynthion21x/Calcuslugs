import src.core.core as g
import src.core.content.contentManager as content
import src.shared.logger as l

import random

import src.math.functions

lines = open(content.Text("title")).read().splitlines()
selection = random.choice(lines)

# Main Loop

main = g.Game(selection)

main.coreLoop()

# Logger should be cleaned up

print("Goodbye World")