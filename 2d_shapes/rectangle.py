def area_rectangle(length, width):
    """Calculates the area of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

def perimeter_rectangle(length, width):
    """Calculates the perimeter of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)