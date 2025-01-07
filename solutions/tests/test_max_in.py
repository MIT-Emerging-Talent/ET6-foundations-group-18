#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: test_max_in

Description:
    This module contains unit tests for the 'max_in' function defined 
    in the 'max_in.py' module.

Author: Tagwa Hashim

"""


import unittest
from solutions.max_in import max_in


class TestMax_in(unittest.TestCase):
    """Test the max_in function"""

    def test_positive_integers(self):
        """it should return 9 as the maximum number in this list"""

        self.assertEqual(max_in([1, 5, 3, 9, 2]), 9)

    def test_positive_floats(self):
        """it should return 10.5 as the maximum number in this list"""
        self.assertEqual(max_in([10.5, 5.2, 8.7]), 10.5)

    def test_mix_types(self):
        """it should return 1 as the maximum number in this list"""
        self.assertEqual(max_in([1, -5.5, -3]), 1)

    def test_empty_list(self):
        """"""
        with self.assertRaises(ValueError):

            self.assertEqual(max_in([]), "List cannot be empty.")

    def test_single_element_list(self):
        """"""
        self.assertEqual(max_in([5]), 5)

    def test_non_list_input(self):
        """"""
        with self.assertRaises(ValueError):

            self.assertEqual(max_in("not a list"), "Input must be a list.")

    def test_list_with_non_numeric_element(self):
        """"""
        with self.assertRaises(TypeError):

            self.assertEqual(
                max_in([1, 2, "three"]), "List contains non-numeric elements."
            )


if __name__ == "__main__":
    unittest.main()
