def volume_cube(side):
    """Calculates the volume of a cube."""
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side ** 3

def surface_area_cube(side):
    """Calculates the surface area of a cube."""
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return 6 * (side ** 2)