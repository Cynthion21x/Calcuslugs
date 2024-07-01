import src.math.vectors as v
import src.core.content.contentManager as content
import src.shared.constants as c
import pygame

class slug:

    def __init__(self, name, mapF, index):

        self.activePointer = False
        self.map = mapF

        self.gameCoord = v.Vector(index, int(c.GAME_HEIGHT / 3))

        self.position = self.map.grid[self.gameCoord.x][self.gameCoord.y].pos

        data = content.Slug(name)

        self.hp = data["hp"]
        self.speed = data["speed"]

        self.pointerSprite = content.Sprite(data["pointer"])
        self.sprite = content.Sprite(data["sprite"])

        self.direction = 1

        if index > c.GAME_WIDTH / 2:
            self.direction = -1

        self.sprite = pygame.transform.scale(self.sprite, (c.SLUG_SIZE, c.SLUG_SIZE))
        self.pointerSprite = pygame.transform.scale(self.pointerSprite, (c.SLUG_SIZE, c.SLUG_SIZE))
        self.flippedSprtie = pygame.transform.flip(self.sprite, True, False)


    def render(self, display):

        pos = v.sub(self.position, v.Vector(c.SLUG_SIZE/2, c.SLUG_SIZE))

        if self.direction == 1:

            display.blit(self.sprite, pos.value())

        else:

            display.blit(self.flippedSprtie, pos.value())

        if (self.activePointer):

            display.blit(self.pointerSprite, v.sub(pos, v.Vector(0, c.SLUG_SIZE)).value())

        pygame.draw.rect(display, c.Colours.RED, pygame.Rect(self.position.x, self.position.y, c.TILE_SIZE, c.TILE_SIZE))

    def run(self):

        pass

    def move(self, deltatime, vector):

        if (self.activePointer):

            self.activePointer = False

        self.direction = vector.x

        self.position = v.add(self.position, v.mult(vector, deltatime * self.speed))
