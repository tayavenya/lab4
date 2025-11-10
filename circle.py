import math

def area(r):
    """
    Calculate the area of a circle.
    Args:
        r (float): Radius of the circle.
    Returns:
        float: Area of the circle.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculate the perimeter (circumference) of a circle.
    Args:
        r (float): Radius of the circle.
    Returns:
        float: Circumference of the circle.
    """
    return 2 * math.pi * r