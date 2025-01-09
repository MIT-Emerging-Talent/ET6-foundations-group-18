"""
A module for calculating the area of a circle.

Module contents:
    - area_of_circle: calculates the area of a circle given its radius.

Created on 01 04 2025
@author: Raghad
"""
import math

def area_of_circle(radius: float) -> float:
    """Calculate the area of a circle given its radius.

    Parameters:
        radius: float, the radius of the circle

    Returns -> float: area of the circle

    Raises:
        ValueError: if the radius is negative

    >>> area_of_circle(5)
    78.53981633974483
    >>> area_of_circle(0)
    0.0
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    return math.pi * radius**2

if __name__ == "__main__":
    radius = 5
    area = area_of_circle(radius)
    print("Area of the circle:", area)
