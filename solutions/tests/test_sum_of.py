#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_of function.

@author: Tagwa Hashim
"""

import unittest

from solutions.sum_of import sum_of


class TestSumOf(unittest.TestCase):
    """Test the sum_of function"""

    def test_add_integers(self):
        """Test sum_of of two integers."""
        self.assertEqual(sum_of(7, 12), 19)

    def test_add_floats(self):
        """Test sum_of of two floats."""
        self.assertEqual(sum_of(1.6, 3.3), 4.9)

    def test_add_mixtype(self):
        """Test sum_of of integer and float."""
        self.assertEqual(sum_of(3, 2.05), 5.05)

    def test_add_zero(self):
        """Test sum_of with zero."""
        self.assertEqual(sum_of(0, 5), 5)
        self.assertEqual(sum_of(5, 0), 5)

    def test_add_negative_numbers(self):
        """Test sum_of with negative numbers."""
        self.assertEqual(sum_of(-3, -5), -8)
        self.assertEqual(sum_of(-3, 5), 2)

    def test_invalid_input_type_num(self):
        """Test with invalid input type for num1 or num2, should raise assertion error"""

        with self.assertRaises(AssertionError):
            sum_of("hello", 2)
            sum_of(18, "hello")


if __name__ == "__main__":
    unittest.main()
