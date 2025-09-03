import math

def volume_cylinder(radius, height):
    """Calculates the volume of a cylinder."""
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")
    return math.pi * (radius ** 2) * height

def surface_area_cylinder(radius, height):
    """Calculates the surface area of a cylinder."""
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")
    return 2 * math.pi * radius * (radius + height)