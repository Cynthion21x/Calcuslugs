import math
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

    # Vector Addition
    def add(self, vector):
        
        self.x += vector.x
        self.y += vector.y

        return self

    # Multiply by constant
    def multC(self, constant):

        self.x *= constant
        self.y *= constant

        return self
    
    # Multiply by vector
    def multV(self, vector):
        
        newM = self.distance() * vector.distance()
        newA = self.angle() * vector.angle()

        return FromBearing(newA, newM)
    
    # Vector set to values from 0-1
    def normalize(self):

        return FromBearing(self.angle(), 1)

    # Return value as tuple
    def value(self):

        return (self.x, self.y)
    
# Generator Functions
def FromBearing(angle, magnitude):

    horizontalComp = math.cos(angle) * magnitude
    verticalComp = math.sin(angle) * magnitude

    return Vector(horizontalComp, verticalComp)

# Useful constants

Up = Vector(0, 1)
Down = Vector(0, -1)
Left = Vector(-1, 0)
Right = Vector(1, 0)

One = Vector(1, 1)
Zero = Vector(0, 0)

