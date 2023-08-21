import os
import pygame
import Game.src.shared.constants as c
import Game.src.client.game as g

import random

f = open(c.ASSETS_PATH + "\\titleText.txt", "r")

line = next(f)

for num, aline in enumerate(f, 2):

    if random.randrange(num):

        continue

    line = aline


f.close()

main = g.Game(line)

main.coreLoop()

print("dont cringe a ninja")