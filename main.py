import src.shared.constants as c
import pygame
import time
import random

# SPLASH SCREEN

pygame.init()

splash = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.NOFRAME)
splash.blit(pygame.image.load(c.ASSETS_PATH + "\\splash.png"), (0, 0))
pygame.display.flip()

# LOAD GAME

import src.core.core as g
import src.core.content.contentManager as content
import src.core.content.config as conf
import src.shared.logger as l

with open(content.Text("title")) as file:
    lines = file.read().splitlines()
    selection = random.choice(lines)

time.sleep(1)

# Main Loop

main = g.Game(selection)

main.coreLoop()

# Logger should be cleaned up

print("Goodbye World")