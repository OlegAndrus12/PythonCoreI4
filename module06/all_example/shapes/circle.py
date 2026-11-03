import math

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

def _validate(radius):
    if radius <= 0:
        raise ValueError("radius must be positive")
