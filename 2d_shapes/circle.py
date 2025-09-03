import math

def area_circle(radius):
    """Calculates the area of a circle."""
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * (radius ** 2)

def circumference(radius):
    """Calculates the circumference of a circle."""
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * math.pi * radius