import src.shared.constants as c
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.UI.elements as elements
import src.core.content.config as config
from src.core.entities import tilemap, slug
import src.core.Input.inputManager as Input
import random
import pygame
import math

class game:

    def __init__(self, game):

        self.game = game

        self.circlePos = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        # TURN TRUE -> PLAYER 1
        # TURN FALSE -> PLAYER 2

        self.started = False

        self.ui()

    def generateBackground(self):

        backgrounds = []
        keys = content.fetch().spriteBase.keys()

        for key in keys:

            if key.startswith('background\\'):

                backgrounds.append(content.Sprite(key))

        self.selectedBackground = backgrounds[random.randrange(0, len(backgrounds))]
        # Blur takes long time so need to store them and call them back
        # self.selectedBackground = elements.blur(self.selectedBackground, 5)
        self.background = elements.photo(v.Vector(((c.SCREEN_WIDTH - c.GAME_WIDTH_REAL) / 2) , 25), v.Vector(c.GAME_WIDTH_REAL, c.GAME_HEIGHT_REAL), self.selectedBackground)
    
    def ui(self):

        self.mainBox = elements.photo(v.Zero, v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), content.Sprite("UI\\gameBox"))

        # Generator function here

        self.clock = elements.text(

            v.Vector((c.SCREEN_WIDTH - 200) / 2, 10),
            v.Vector(200, 10), "10:00",
            content.Font("Sobiscuit")

        )

    def start(self):
         
        self.started = True
        self.turnTimer = int(config.getOption("turnTime"))

        self.turn = True

        self.player1Index = self.player2Index = 0

        # Pick background
        self.generateBackground()

        # Generate map
        params = [
            random.randrange(int( c.GAME_WIDTH /10 ), int( c.GAME_WIDTH /3 )),
            random.randrange(int( c.GAME_WIDTH /10 ), int( c.GAME_WIDTH /3 )),
            random.randrange(int( c.GAME_WIDTH /10 ), int( c.GAME_WIDTH /3 )),
            random.uniform(0, 3 * math.pi),
            random.uniform(0, 3 * math.pi),
            random.uniform(0, 3 * math.pi),
            random.randrange(int( c.GAME_HEIGHT /7 ), int( c.GAME_HEIGHT /3 )) / 2,
            random.randrange(int( c.GAME_HEIGHT /7 ), int( c.GAME_HEIGHT /3 )) / 2,
            random.randrange(int( c.GAME_HEIGHT /7 ), int( c.GAME_HEIGHT /3 )) / 2
        ]

        colour = pygame.transform.average_color(self.selectedBackground)

        self.grid = tilemap.Tilemap(c.GAME_WIDTH, c.GAME_HEIGHT, params, colour)

        # Spawn in players
        keys = content.fetch().slugBase.keys()

        self.teamTrue = []
        self.teamFalse = []


        for key in keys:

            xPos = random.randint(0, c.GAME_WIDTH-1)

            if content.Slug(key)["team"] == True:

                self.teamTrue.append(slug.slug(key, self.grid, xPos))

            else:

                self.teamFalse.append(slug.slug(key, self.grid, xPos))

        self.activeSlug = self.teamTrue[self.player1Index]
        self.player1Index += 1

    def run(self):

        # Start func
        if not self.started:
            self.start()

        # Game logic
        self.turnTimer -= self.game.deltaTime

        clockText = str(int(self.turnTimer // 60))
        clockSecond = str(int(self.turnTimer % 60))

        if len(clockSecond) == 1:

            clockSecond = "0" + clockSecond

        if len(clockText) == 1:

            clockText = "0" + clockText

        self.clock.updateText(clockText + ":" + clockSecond)

        if self.turnTimer < 1:

            # New turn
            self.turnTimer = int(config.getOption("turnTime"))
            self.turn = not self.turn

            if self.turn == True:

                self.activeSlug = self.teamTrue[self.player1Index]
                self.player1Index += 1

            else:

                self.activeSlug = self.teamFalse[self.player2Index]
                self.player2Index += 1

        if Input.fetch().KEY_DOWN == pygame.K_ESCAPE:
            self.start()

        if Input.fetch().KEY_HOLD == pygame.K_LEFT:
            self.activeSlug.move(self.game.deltaTime, v.Vector(-1, 0))

        if Input.fetch().KEY_HOLD == pygame.K_RIGHT:
            self.activeSlug.move(self.game.deltaTime, v.Vector(1, 0))

        for s1 in self.teamTrue:

            s1.run()

        for s2 in self.teamFalse:

            s2.run()


        # ----- Game Render ----- 

        self.game.display.fill(c.Colours.GREY)

        # Background
        pygame.draw.rect(self.game.display, c.Colours.BLUE, pygame.Rect((c.SCREEN_WIDTH-980) / 2, 25, 980, 400))
        self.background.render(self.game.display)

        # Terrain

        self.grid.render(self.game.display)

        # Slugs
    
        for s1 in self.teamTrue:

            s1.render(self.game.display)

        for s2 in self.teamFalse:

            s2.render(self.game.display)

        # UI render
        self.mainBox.render(self.game.display)
        self.clock.render(self.game.display)
