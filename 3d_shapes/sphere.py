import math

def volume_sphere(radius):
    """Calculates the volume of a sphere."""
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return (4/3) * math.pi * (radius ** 3)