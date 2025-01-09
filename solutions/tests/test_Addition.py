#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the Addition function.

@author: Tagwa Hashim
"""

import unittest

from solutions.addition import addition


class TestAddition(unittest.TestCase):
    """Test the addition function"""

    def test_add_integers(self):
        """Test addition of two integers."""
        self.assertEqual(addition(7, 12), 19)

    def test_add_floats(self):
        """Test addition of two floats."""
        self.assertEqual(addition(1.6, 3.3), 4.9)

    def test_add_mixtype(self):
        """Test addition of integer and float."""
        self.assertEqual(addition(3, 2.05), 5.05)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(addition(0, 5), 5)
        self.assertEqual(addition(5, 0), 5)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(addition(-3, -5), -8)
        self.assertEqual(addition(-3, 5), 2)

    def test_invalid_input_type_num(self):
        """Test with invalid input type for num1 or num2."""

        with self.assertRaises(AssertionError):
            addition("hello", 2)
            addition(18, "hello")


if __name__ == "__main__":
    unittest.main()
