import unittest
from solutions.area_of_circle import area_of_circle

class TestCircleArea(unittest.TestCase):
    """Unit tests for the area_of_circle function."""
    
    def test_positive_radius(self):
        """Test the function with positive radius values."""
        self.assertAlmostEqual(area_of_circle(5), 78.53981633974483)
        self.assertAlmostEqual(area_of_circle(10), 314.1592653589793)
        
    def test_zero_radius(self):
        """Test the function with a zero radius."""
        self.assertEqual(area_of_circle(0), 0.0)
        
    def test_large_radius(self):
        """Test the function with a very large radius."""
        self.assertAlmostEqual(area_of_circle(1000), 3141592.653589793)

if __name__ == '__main__':
    unittest.main()
