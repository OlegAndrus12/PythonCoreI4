def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def _validate(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("dimensions must be positive")
