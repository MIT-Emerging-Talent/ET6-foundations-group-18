"""
Module: test_binary_decimal_conversion
contains test cases for the solution code.

Created by Muna Sattouf on January 2, 2024
Completed on January 2, 2024
"""
import unittest
from binary_decimal_conversion import decimal_to_binary, binary_decimal_conversion, binary_to_decimal

class TestBinaryDecimalConversion(unittest.TestCase):
    
    def test_decimal_to_binary(self):
        """Should convert positive decimal numbers to binary"""
        self.assertEqual(decimal_to_binary(10), '1010')
                
    def test_binary_to_decimal(self):
        """Should convert positive binary to decimal"""
        self.assertEqual(binary_to_decimal(10011101), 157) 
        
    def test_zero_decimal_to_binary(self):
        """should return 0"""
        self.assertEqual(decimal_to_binary(0), '0')
        
    def test_zero_binary_to_decimal(self):
        """should return 0"""
        self.assertEqual(binary_to_decimal(0), '0')
    
    def test_large_decimal_to_binary(self):
        """Should correctly handle large decimal numbers"""
        self.assertEqual(decimal_to_binary(1000000), '11110100001001000000')
        
    def test_large_binary_to_decimal(self):
        """Should correctly handle large binary numbers"""
        self.assertEqual(binary_to_decimal('11110100001001000000'), 1000000)
    
    def test_binarydecimalconversion_decimal(self):
        """Should convert binary to decimal when conversion type is decimal"""
        self.assertEqual(binary_decimal_conversion('decimal', '10011101'), 157)
    
    def test_binarydecimalconversion_binary(self):
        """Should convert decimal to binary when conversion type is binary"""
        self.assertEqual(binary_decimal_conversion('binary', '392'), 110001000)
        
    def test_invalid_decimal_input(self):
        """Should raise ValueError for non-integer decimal input"""
        with self.assertRaises(ValueError):
            decimal_to_binary("notAnumber")
    
    def test_invalid_binary_input(self):
        """Should raise ValueError for non-binary input"""
        with self.assertRaises(ValueError):
            binary_to_decimal("1234")
            
    def test_invalid_decimal_conversion_input(self):
        """Should raise ValueError if a non-binary string is provided to convert to decimal"""
        with self.assertRaises(ValueError):
            binary_decimal_conversion("decimal", "1020")
            
    def test_invalid_binary_conversion_input(self):
        """Should raise ValueError if a non-integer was provided to convert to binary"""
        with self.assertRaises(ValueError):
            binary_decimal_conversion('binary', 'word')
            
if __name__ == '__main__':
    unittest.main()