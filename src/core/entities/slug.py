import src.math.vectors as v
import src.core.content.contentManager as content
import src.shared.constants as c
import src.shared.logger as l
import src.core.content.config as config
import pygame

class slug:

    def __init__(self, name, mapF, index):

        self.activePointer = False
        self.map = mapF

        self.gameCoord = v.Vector(index, int(c.GAME_HEIGHT / 3))

        self.boundsCheck()

        self.position = self.map.grid[self.gameCoord.x][self.gameCoord.y].pos

        self.originCord = self.position

        data = content.Slug(name)

        self.hp = data["hp"]
        self.maxHp = self.hp
        self.speed = data["speed"]

        self.pointerSprite = content.Sprite(data["pointer"])
        self.sprite = content.Sprite(data["sprite"])

        self.direction = 1

        if index > c.GAME_WIDTH / 2:
            self.direction = -1

        self.sprite = pygame.transform.scale(self.sprite, (c.SLUG_SIZE, c.SLUG_SIZE))
        self.pointerSprite = pygame.transform.scale(self.pointerSprite, (c.SLUG_SIZE, c.SLUG_SIZE))
        self.flippedSprtie = pygame.transform.flip(self.sprite, True, False)

    def getCoord(self, x, y):

        try:
            return self.map.grid[x][y]
        except:
            l.Logger.log("slug out of bounds", logLevel=c.Logs.ERROR)
            self.position = self.originCord
            return self.map.grid[0][0]

    def boundsCheck(self):

        if self.gameCoord.x < 0:
            self.gameCoord.x = 0
            self.normalizePos()

        if self.gameCoord.y < 0:
            self.gameCoord.y = 0
            self.normalizePos()

        if self.gameCoord.x > c.GAME_WIDTH-1:
            self.gameCoord.x = c.GAME_WIDTH-1
            self.normalizePos()

        if self.gameCoord.y > c.GAME_HEIGHT-1:
            self.gameCoord.y = c.GAME_HEIGHT-1
            self.normalizePos()

    def renderCheckBox(self, display):

        # show slugs tile representation
        tilePos = self.getCoord(self.gameCoord.x, self.gameCoord.y).pos
        pygame.draw.rect(display, c.Colours.RED, pygame.Rect(tilePos.x, tilePos.y, c.TILE_SIZE, c.TILE_SIZE))
        pygame.draw.rect(display, c.Colours.BLUE, pygame.Rect(self.position.x, self.position.y, c.TILE_SIZE, c.TILE_SIZE))

    def render(self, display):

        pos = self.getCoord(self.gameCoord.x, self.gameCoord.y+1).pos
        pos = v.sub(pos, v.Vector((c.SLUG_SIZE-c.TILE_SIZE)/2, c.SLUG_SIZE))

        if self.direction == 1:

            display.blit(self.sprite, pos.value())

        else:

            display.blit(self.flippedSprtie, pos.value())

        if (self.activePointer):

            display.blit(self.pointerSprite, v.sub(pos, v.Vector(0, c.SLUG_SIZE)).value())

        if config.getOption("showSlugCollider"):
            self.renderCheckBox(display)

        # HP Bar

        hpRect = pygame.Rect(
            pos.x, #- (c.SLUG_SIZE/2),
            pos.y + c.SLUG_SIZE + 10,
            c.SLUG_SIZE,
            10
        )

        pygame.draw.rect(display, c.Colours.RED, hpRect)

        hpRemainingRect = pygame.Rect(
            pos.x,
            pos.y + c.SLUG_SIZE + 10,
            c.SLUG_SIZE * self.hp / self.maxHp,
            10  
        )

        pygame.draw.rect(display, c.Colours.GREEN, hpRemainingRect)

    def normalizePos(self):

        self.position = self.getCoord(self.gameCoord.x, self.gameCoord.y).pos

    def run(self, deltatime):

        self.gameCoord = v.normalToGameCoord(self.position)

        self.boundsCheck()

        if self.getCoord(self.gameCoord.x, self.gameCoord.y+1).none:

            self.position = v.add(self.position, v.Vector(0, c.GRAVITY * deltatime))

        elif self.getCoord(self.gameCoord.x, self.gameCoord.y+1).lava:

            self.hp -= 70 * deltatime

        if not (self.getCoord(self.gameCoord.x, self.gameCoord.y).none):

            while not (self.getCoord(self.gameCoord.x, self.gameCoord.y).none):

                self.position = v.sub(self.position, v.Vector(0, c.TILE_SIZE * 10 * deltatime))
                self.gameCoord = v.normalToGameCoord(self.position)

    def move(self, deltatime, vector):

        if (self.activePointer):

            self.activePointer = False

        self.direction = vector.x

        self.position = v.add(self.position, v.mult(vector, deltatime * self.speed))
