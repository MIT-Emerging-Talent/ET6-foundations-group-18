"""
Module: Binary to Hexadecimal Converter

It validates the input to ensure that it contains only binary digits (0s and 1s) and performs the conversion
accurately.

Author: Marc Darazi
"""

import unittest
from solutions.binary_to_hex import binary_to_hex


class TestBinaryToHex(unittest.TestCase):
    """
    Testing the binary-to-hex function.
    """
    # Unit Tests
    def test_binary_to_hex_valid(self):
        """
        Test binary_to_hex with valid binary input.
        Asserts the correct hexadecimal output is produced.
        it should give D
        """
        assert binary_to_hex("1101") == "D"

    def test_binary_to_hex_large(self):
        """
        Test binary_to_hex with a larger binary input.
        Asserts the correct hexadecimal output is produced.
        """
        assert binary_to_hex("11110000") == "F0"

    def test_binary_to_hex_minimum(self):
        """
        Test binary_to_hex with the smallest valid binary input.
        Asserts the correct hexadecimal output is produced.
        """
        assert binary_to_hex("0") == "0"

    def test_binary_to_hex_invalid(self):
        """
        Test binary_to_hex with invalid input containing non-binary characters.
        Asserts that a ValueError is raised.
        """
        try:
            binary_to_hex("11012")
        except ValueError as e:
            assert str(e) == "Input must be a binary string containing only 0s and 1s."
        else:
            assert False, "ValueError was not raised for invalid input."
