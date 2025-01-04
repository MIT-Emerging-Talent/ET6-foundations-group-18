"""
A module for calculating the area of a circle.

Module contents:
    - calculate_circle_area: calculates the area of a circle given its radius.

Created on 01 04 2025
@author: Raghad
"""
import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius.

    Parameters:
        radius: float, the radius of the circle

    Returns -> float: area of the circle

    Raises:
        ValueError: if the radius is negative

    >>> calculate_circle_area(5)
    78.53981633974483
    >>> calculate_circle_area(0)
    0.0
    >>> calculate_circle_area(-1)
    Traceback (most recent call last):
        ...
    ValueError: Radius cannot be negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    return math.pi * radius**2

if _name_ == "_main_":
    radius = 5
    area = calculate_circle_area(radius)
    print("Area of the circle:", area)
