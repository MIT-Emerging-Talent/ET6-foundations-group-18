import unittest
import math
from solutions.area_of_circle import calculate_circle_area
# Assuming the function is already defined as:
# def calculate_circle_area(radius):
#     if radius < 0:
#         return "Radius cannot be negative"
#     area = math.pi * radius**2
#     return area

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
