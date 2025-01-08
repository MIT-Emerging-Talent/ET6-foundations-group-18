"""
Unit test module for area_of_circle.py

Module contents:
    - Unit Test cases for calculating the area of circle

Created on 01 01 2025
@author: Raghad
"""

import unittest
import math
from solutions.area_of_circle import calculate_circle_area

class TestCircleArea(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(5), math.pi * 5**2)
        self.assertAlmostEqual(calculate_circle_area(10), math.pi * 10**2)
        
    def test_zero_radius(self):
        self.assertEqual(calculate_circle_area(0), 0)
        
    def test_negative_radius(self):
        self.assertEqual(calculate_circle_area(-5), "Radius cannot be negative")
        
    def test_large_radius(self):
        self.assertAlmostEqual(calculate_circle_area(1000), math.pi * 1000**2)

if __name__ == '__main__':
    unittest.main()
