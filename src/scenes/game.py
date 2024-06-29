import src.shared.constants as c
import src.core.content.contentManager as content
import src.math.vectors as v
import src.core.UI.elements as elements
import src.core.content.config as config
import src.core.entities.tilemap as tiles
import src.core.Input.inputManager as Input
import random
import pygame
import math

class game:

    def __init__(self, game):

        self.game = game

        self.circlePos = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        # TURN 1 -> PLAYER 1
        # TURN 2 -> PLAYER 2

        self.turn = 1

        self.started = False

        self.ui()
    
    def ui(self):

        self.mainBox = elements.photo(v.Zero, v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), content.Sprite("UI\\gameBox"))
        self.background = elements.photo(v.Vector(0 , 25), v.Vector(c.GAME_WIDTH, c.GAME_HEIGHT), content.Sprite("background\\BubbleSeaFloorBG"))
        self.clock = elements.text(

            v.Vector((c.SCREEN_WIDTH - 200) / 2, 10),
            v.Vector(200, 10), "10:00",
            content.Font("Sobiscuit")

        )

    def start(self):
         
        self.started = True
        self.turnTimer = int(config.getOption("turnTime"))

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

        self.grid = tiles.Tilemap(c.GAME_WIDTH, c.GAME_HEIGHT, params)

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

        if Input.fetch().KEY_DOWN == pygame.K_ESCAPE:
            self.start()


        # Game Render

        self.game.display.fill(c.Colours.GREY)

        # Background
        pygame.draw.rect(self.game.display, c.Colours.BLUE, pygame.Rect((c.SCREEN_WIDTH-980) / 2, 25, 980, 400))
        self.background.render(self.game.display)

        # Terrain

        self.grid.render(self.game.display)

        # UI render
        self.mainBox.render(self.game.display)
        self.clock.render(self.game.display)
