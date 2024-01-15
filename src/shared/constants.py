import pygame
import os

# Assets Path

ASSETS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', "assets")

# Program Data

DATA_PATH = os.path.join(os.getenv('APPDATA'), '..', 'LocalLow', 'Cynthion21x', 'calcuslugs')

# Colours

class Colours:

    pass

# Display

SCREEN_NAME = "calcuslugs"
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 585

FRAME_RATE = 60
CLICK_DELAY = 5

# States

class States:

    pass

# Keys

NO_KEY = "None"