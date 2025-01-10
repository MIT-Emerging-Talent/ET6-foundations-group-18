"""
Test for the leap_year function
Created and completed by Muna Sattouf on January 10, 2024
"""

import unittest
from leap_year import leap_year

class TestLeapYear(unittest.TestCase):
    """
    Test cases for the leap_year function
    """
    
    def test_divisibility_by_4(self):
        """
        Tests a year is divisible by 4 but not 100
        """
        self. assertTrue(leap_year(2024))
        
    def test_not_leap_divisible_by_100(self):
        """
        Tests a year divisible by 100 but not 400
        """
        self.assertFalse(leap_year(1900))
        
    def test_leap_divisible_by_400(self):
        """
        Tests a year divisible by 400 
        """
        self.assertTrue(leap_year(2000))
        
    def test_not_leap_not_divisble_by_4(self):
        """
        Tests a year not divisble by 4
        """
        self.assertFalse(leap_year(2023))
        
    def test_invalid_type(self):
        """
        A ValueError should be raised if type is not integer
        """
        with self.assertRaises(ValueError):
            leap_year("hi")
        
    def test_invalid_negative(self):
        """
        A value error must be rasied if the year is a negative integer
        """
        with self.assertRaises(ValueError):
            leap_year(-175)
            
if __name__=="__main__":
    unittest.main()