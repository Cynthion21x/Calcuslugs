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

    BACKGROUND = pygame.Color(5, 4, 59)

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

FRAME_RATE = 60
CLICK_DELAY = 5

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
    SIN = 12       # Sin()
    COS = 13       # Cos()
    TAN = 14       # Tan()

    LN = 15        # Ln()

    NUM = 18
    NEG = 19
    PI = 16        # pi
    E = 17         # e


# Keys

NO_KEY = -1