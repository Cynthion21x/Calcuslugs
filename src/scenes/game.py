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
import src.math.functions as func
import src.shared.logger as l

class game:

    def __init__(self, game):

        self.game = game

        self.circlePos = v.mult(v.Vector(c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0.5)

        # TURN TRUE -> PLAYER 1
        # TURN FALSE -> PLAYER 2

        self.started = False
        self.evalueated = False
        self.func = None
        self.renderLine = False
        self.const = 0

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

        self.formulaBox = elements.textBox(v.Vector(200, 475), v.Vector(300, 40), "", content.Font("default"))

        self.clock = elements.text(

            v.Vector((c.SCREEN_WIDTH - 200) / 2, 10),
            v.Vector(200, 10), "10:00",
            content.Font("Sobiscuit")

        )

        gunboxPos = v.Vector(590, 450)
        gunboxSize = v.Vector(400, 100)

        gunElements = []

        guns = list(content.fetch().gunBase.keys())
        gunCount = len(guns)

        for i in range(0, gunCount):

            wepon = content.Gun(guns[i])

            gunVectorSize = v.Vector(gunboxSize.x / gunCount, gunboxSize.x / gunCount)
            gunVectorPos = v.add(gunboxPos, v.Vector(i * gunboxSize.x / gunCount , -gunVectorSize.y/2 + gunboxSize.y/2))

            image = elements.photo(gunVectorPos, gunVectorSize, content.Sprite(wepon["sprite"]), True)
            hover = elements.photo(gunVectorPos, gunVectorSize, pygame.transform.rotate(content.Sprite(wepon["sprite"]), 10), True)

            gunElements.append(elements.button(
                gunVectorPos,
                gunVectorSize,
                self.shootGun,
                image,
                hover
            ))

        self.guns = elements.group(gunElements)

    def shootGun(self, id):

        pass

    def generateSafeCoord(self, team):

        # Need to generate some smarter bounds for niche scenearios
        # Eg: half the map is submerged in lava

        if team:
            xPos = random.randint(int(c.GAME_WIDTH/2-1), int(c.GAME_WIDTH-1))
        else:
            xPos = random.randint(0, int(c.GAME_WIDTH/2-1))

        while self.grid.mapFunc(xPos + c.GAME_WIDTH / 2) > (c.GAME_HEIGHT / 1.1):

            if team:
                xPos = random.randint(int(c.GAME_WIDTH/2-1), int(c.GAME_WIDTH-1))
            else:
                xPos = random.randint(0, int(c.GAME_WIDTH/2-1))

        return int(xPos)


    def start(self):
         
        self.started = True
        self.turnTimer = config.getOption("turnTime")

        self.turn = True

        self.player1Index = self.player2Index = 0

        # Pick background
        self.generateBackground()

        # Generate map
        params = [
            random.randrange(int( c.GAME_WIDTH /10 ), int( c.GAME_WIDTH /3 )), # Frequency
            random.randrange(int( c.GAME_WIDTH /4 ), int( c.GAME_WIDTH /2 )),
            random.randrange(int( c.GAME_WIDTH /17 ), int( c.GAME_WIDTH /12 )),
            random.uniform(0, 2 * math.pi),
            random.uniform(0, 2 * math.pi),
            random.uniform(0, 2 * math.pi),
            random.randrange(int( c.GAME_HEIGHT /4 ), int( c.GAME_HEIGHT /2 )) / 2, # Height
            random.randrange(int( c.GAME_HEIGHT /6 ), int( c.GAME_HEIGHT /3 )) / 2,
            random.randrange(int( c.GAME_HEIGHT /10 ), int( c.GAME_HEIGHT /5 )) / 2
        ]

        colour = pygame.transform.average_color(self.selectedBackground)

        self.grid = tilemap.Tilemap(c.GAME_WIDTH, c.GAME_HEIGHT, params, colour)

        # Spawn in players
        keys = content.fetch().slugBase.keys()

        self.teamTrue = []
        self.teamFalse = []

        for key in keys:

            if content.Slug(key)["team"] == True:

                xPos = self.generateSafeCoord(True)
                self.teamTrue.append(slug.slug(key, self.grid, xPos))

            else:

                xPos = self.generateSafeCoord(False)
                self.teamFalse.append(slug.slug(key, self.grid, xPos))                

        self.activeSlug = self.teamTrue[self.player1Index]
        self.player1Index += 1
        self.activeSlug.activePointer = True

        if self.player1Index >= len(self.teamTrue)-1:
            self.player1Index = 0

    def run(self):

        # Start func
        if not self.started:
            self.start()

        # Game logic

        if len(self.teamTrue) == 0:

            #loose screen
            self.game.GameState = c.States.VICTORY
            self.game.victory.team = False

        elif len(self.teamFalse) == 0:

            #loose screen
            self.game.GameState = c.States.VICTORY
            self.game.victory.team = True

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
            self.activeSlug.activePointer = False

            self.formulaBox.input = ""
            self.evalueated = False
            self.formulaBox.typing = False

            if self.turn == True:

                self.activeSlug = self.teamTrue[self.player1Index]
                self.activeSlug.activePointer = True
                self.player1Index += 1

                if self.player1Index >= len(self.teamTrue)-1:
                    self.player1Index = 0

            else:

                self.activeSlug = self.teamFalse[self.player2Index]
                self.activeSlug.activePointer = True
                self.player2Index += 1

                if self.player2Index >= len(self.teamFalse)-1:
                    self.player2Index = 0

        if Input.fetch().KEY_DOWN == pygame.K_ESCAPE:
            self.start()

        if Input.fetch().KEY_HOLD == pygame.K_LEFT:
            self.activeSlug.move(self.game.deltaTime, v.Vector(-1, 0))

        if Input.fetch().KEY_HOLD == pygame.K_RIGHT:
            self.activeSlug.move(self.game.deltaTime, v.Vector(1, 0))

        for s1 in self.teamTrue:

            s1.run(self.game.deltaTime)
            if s1.hp <= 0:
                self.teamTrue.remove(s1)

        for s2 in self.teamFalse:

            s2.run(self.game.deltaTime)
            if s2.hp <= 0:
                self.teamTrue.remove(s2)

        self.formulaBox.run(self.game.deltaTime)

        formula = self.formulaBox.input

        if not self.formulaBox.typing:

            if not self.evalueated:

                try:
                    self.func = func.Function(formula)
                    self.renderLine = True
                    self.func.evaluate(random.randint(0, 10))

                except:

                    formula = formula.strip()

                    if formula != "":

                        l.Logger.log("Malformed Function", formula, c.Logs.WARNING)

                    self.renderLine = False

                self.evalueated = True

        else:

            self.evalueated = False

        # Generate line

        if self.renderLine:

            gameOffset = v.Vector(int((c.SCREEN_WIDTH-980) / 2), 25)

            slugPos = self.activeSlug.getCoord(self.activeSlug.gameCoord.x, self.activeSlug.gameCoord.y).pos

            self.linePoints = []

            if (slugPos.x) < (c.GAME_WIDTH_REAL/2):

                const = c.GAME_HEIGHT_REAL - slugPos.y + (c.SLUG_SIZE/4) - self.func.evaluate(0)

                for i in range(int(slugPos.x), c.GAME_WIDTH_REAL+c.SLUG_SIZE):

                    x =  i - int(slugPos.x)
                    y = (c.GAME_HEIGHT_REAL-(self.func.evaluate(x)))-const

                    coord = v.Vector(i, y)

                    self.linePoints.append(coord.value())
                    self.renderLine = True

            else:

                const = c.GAME_HEIGHT_REAL - slugPos.y + (c.SLUG_SIZE/4) - self.func.evaluate(0)

                for i in range(int(slugPos.x), gameOffset.x, -1):

                    x = int(slugPos.x) - i
                    y = (c.GAME_HEIGHT_REAL-(self.func.evaluate(x)))-const

                    coord = v.Vector(i, y)

                    self.linePoints.append(coord.value())
                    self.renderLine = True       


        # ----- Game Render ----- 

        self.game.display.fill(c.Colours.GREY)

        # Background
        pygame.draw.rect(self.game.display, c.Colours.BLUE, pygame.Rect((c.SCREEN_WIDTH-980) / 2, 25, 980, 400))
        self.background.render(self.game.display)

        # Terrain

        self.grid.render(self.game.display)

        if self.renderLine:
            pygame.draw.lines(self.game.display, c.Colours.LASER_PREVIEW, False, self.linePoints, 5)


        # Slugs
    
        for s1 in self.teamTrue:

            s1.render(self.game.display)

        for s2 in self.teamFalse:

            s2.render(self.game.display)

        # UI render
        self.mainBox.render(self.game.display)
        self.clock.render(self.game.display)
        self.formulaBox.render(self.game.display)
        self.guns.run(self.game.display)