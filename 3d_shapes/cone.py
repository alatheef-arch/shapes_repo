import math

def volume_cone(radius, height):
    """Calculates the volume of a cone."""
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")
    return (1/3) * math.pi * (radius ** 2) * height

def lateral_surface_area_cone(radius, height):
    """Calculates the lateral surface area of a cone."""
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")
    slant_height = math.sqrt((radius ** 2) + (height ** 2))
    return math.pi * radius * slant_height

def total_surface_area_cone(radius, height):
    """Calculates the total surface area of a cone."""
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers.")
    slant_height = math.sqrt((radius ** 2) + (height ** 2))
    return math.pi * radius * (radius + slant_height)