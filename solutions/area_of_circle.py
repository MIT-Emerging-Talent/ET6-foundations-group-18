"""
A module for calculating the area of a circle.

Module contents:
    - area_of_circle: calculates the area of a circle given its radius.

Created on 01 04 2025
@author: Raghad
"""

import math


# Define a function to calculate the area of a circle.
def area_of_circle(radius: float) -> float:
    """Calculate the area of a circle given its radius.

    Parameters:
        radius: float, the radius of the circle

    Returns -> float: area of the circle

    Raises:
        ValueError: if the radius is negative

    Examples:
        >>> area_of_circle(5)
        78.53981633974483
        >>> area_of_circle(0)
        0.0
        >>> area_of_circle(3.5)
        38.48451000647496
    """
    # Raise an error if the radius is negative.
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    # Calculate and return the area using the formula: area = π * r^2
    return math.pi * radius**2


# Entry point for script execution
if __name__ == "__main__":
    # Example usage: Calculate the area of a circle with a radius of 5.
    radius = 5
    area = area_of_circle(radius)
    print("Area of the circle:", area)
