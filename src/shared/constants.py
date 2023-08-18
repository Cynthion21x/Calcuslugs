import pygame
import os

# Colours

class Colours:

    # Standard Colours
    CERISE = pygame.Color(222, 49, 99)
    NUCLEAR_SNOT_GREEN = pygame.Color(74, 255, 8)

    # Basic Colours
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    GREY = pygame.Color(128, 132, 140)

    INVISIBLE = pygame.Color(0, 0, 0, 0)
    SHADOW = pygame.Color(0, 0, 0, 71)

    # Sepcialised Colours
    PROJECTILE_PATH = pygame.Color(18, 235, 255)
    BUTTON_NORMAL = pygame.Color(3, 136, 136)
    BUTTON_HOVER = pygame.Color(6, 106, 117)

# Display

SCREEN_NAME = "calcuslugz"
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 585

FRAME_RATE = 60
CLICK_DELAY = 5

# States

class States:

    MAIN_MENU = 1
    LOBBY = 2
    GAME = 3

# Network options

LOCALHOST = "127.0.0.1"
DEFAULT_PORT = "1700"

# Assets Path
ASSETS_PATH = os.path.join(os.path.dirname(__file__) , '..', '..', 'assets')