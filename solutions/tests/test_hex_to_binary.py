import unittest
from hex_to_binary import hex_to_binary

class TestHexToBinary(unittest.TestCase):
    """
    Unit tests for the hex_to_binary function.

    These tests validate that the hex_to_binary function correctly converts
    hexadecimal strings to binary strings, handling both cases with and
    without the '0x' prefix and invalid inputs.
    """
    
    def test_valid_hex_without_prefix(self):
        """
        Test converting a valid hexadecimal string without the '0x' prefix.
        """
        self.assertEqual(hex_to_binary("1A"), "11010")
        
    def test_valid_hex_with_prefix(self):
        """
        Test converting a valid hexadecimal string with the '0x' prefix.
        """
        self.assertEqual(hex_to_binary("0xFF"), "11111111")
        
    def test_single_digit_hex(self):
        """
        Test converting a single digit hexadecimal string.
        """
        self.assertEqual(hex_to_binary("9"), "1001")
        
    def test_hex_with_lowercase_letters(self):
        """
        Test converting a hexadecimal string with lowercase letters.
        """
        self.assertEqual(hex_to_binary("a"), "1010")
        
    def test_invalid_hex_with_non_hex_characters(self):
        """
        Test an invalid hexadecimal string with non-hex characters.
        """
        with self.assertRaises(ValueError):
            hex_to_binary("G1")
            
    def test_empty_string(self):
        """
        Test an empty string as input, which should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            hex_to_binary("")

if __name__ == "_main_":
    unittest.main()
