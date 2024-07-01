import math
import src.shared.constants as c
import src.shared.logger as l

# Vector value with helper functions
class Vector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    # Returns magnitude of vector
    def distance(self):

        x = self.x
        y = self.y
        
        return math.sqrt((x * x) + (y * y))
    
    # Return angle between sides
    def angle(self):

        x = self.x
        y = self.y

        return math.atan(y/x)
    
    # Vector set to values from 0-1
    def normalize(self):

        return FromBearing(self.angle(), 1)

    # Return value as tuple
    def value(self):

        return (self.x, self.y)
    
# Multiply vector by number
def mult(vector1, const):

    return Vector(vector1.x * const, vector1.y * const)

# Add two vectors together
def add(vector1, vector2):
        
    x = vector1.x + vector2.x
    y = vector1.y + vector2.y

    return Vector(x, y)

# Sub two vectors
def sub(vector1, vector2):
        
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y

    return Vector(x, y)

# Generator Functions
def FromBearing(angle, magnitude):

    horizontalComp = math.cos(angle) * magnitude
    verticalComp = math.sin(angle) * magnitude

    return Vector(horizontalComp, verticalComp)

def FromTuple(tup):

    return Vector(tup[0], tup[1])

#GameCoords

def normalToMap(vector):

    return add(vector, Vector((c.SCREEN_WIDTH-980) / 2, 25))
    
def gameToNormalCoord(vector):

    vec = mult(vector, c.TILE_SIZE)
    vec = add(vec, Vector((c.SCREEN_WIDTH-980) / 2, 25))

    return vec

def normalToGameCoord(vector):

    vec = sub(vector, Vector((c.SCREEN_WIDTH-980) / 2, 25))
    vec.x = int(vec.x / c.TILE_SIZE)
    vec.y = int(vec.y / c.TILE_SIZE)

    return vec

# Useful constants

Up = Vector(0, 1)
Down = Vector(0, -1)
Left = Vector(-1, 0)
Right = Vector(1, 0)
One = Vector(1, 1)
Zero = Vector(0, 0)

