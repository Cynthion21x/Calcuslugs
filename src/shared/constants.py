import pygame
import os

# Assets Path

ASSETS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', "assets")

# Program Data

DATA_PATH = os.path.join(os.getenv('APPDATA'), '..', 'LocalLow', 'Cynthion21x', 'calcuslugs')

# Colours

class Colours:

    RED = pygame.Color(204, 39, 61)
    BLUE = pygame.Color(38, 50, 181)
    GREEN = pygame.Color(49, 161, 91)

    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0 ,0)
    GREY = pygame.Color(112, 116, 125)

    BACKGROUND = pygame.Color(5, 4, 59)
    FLOOR = pygame.Color(76, 107, 102)
    LAVA = pygame.Color(219, 85, 13)

# Log Levels

class Logs:

    NORMAL = 0
    ERROR = 1
    WARNING = 2
    TEST = 3

# Display

SCREEN_NAME = "calcuslugs"
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 585

GAME_WIDTH_REAL = 980
GAME_HEIGHT_REAL = 400

TILE_SIZE = 2
GAME_WIDTH = int(GAME_WIDTH_REAL / TILE_SIZE)
GAME_HEIGHT = int(GAME_HEIGHT_REAL / TILE_SIZE)

SLUG_SIZE = 40

# Game constants

FRAME_RATE = 60
CLICK_DELAY = 5
GRAVITY = 150

# States

class States:

    SPLASH = 2
    MENU = 0
    GAME = 1

# Tokens for maths interpreter
    
class tokens:

    ADD = 0        # +
    MULT = 1       # *
    DIV = 2        # /
    SUB = 3        # -

    LBRACKET = 5   # (
    RBRACKET = 6   # )

    POWER = 7      # ^

    VAR = 8        # x

    SQRT = 9       # sqrt()
    LOG = 10       # log()
    ABS = 11       # | |
    ABSFUNC = 20   # abs()
    SIN = 12       # Sin()
    COS = 13       # Cos()
    TAN = 14       # Tan()

    LN = 15        # Ln()

    NUM = 18       # Number
    NEG = 19       # Negative Number
    PI = 16        # pi
    E = 17         # e


# Keys

NO_KEY = -1