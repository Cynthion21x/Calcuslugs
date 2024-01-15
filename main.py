import src.core.game as g
import src.core.content.contentManager as content

import random

# Load Content

loader = content.Content()


# Main Loop

main = g.Game("A game")

main.coreLoop()

print("Goodbye world")