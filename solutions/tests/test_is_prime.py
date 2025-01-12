#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from solutions.is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    """test the is_prime function"""

    def test_0(self):
        """It should evaluate not prime"""
        actual = is_prime(0)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate not prime"""
        actual = is_prime(1)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = is_prime(2)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_4(self):
        """its should evaluate not prime"""
        actual = is_prime(4)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_7(self):
        """It should evaluate prime"""
        actual = is_prime(7)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_9(self):
        """It should evaluate not prime"""
        actual = is_prime(9)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_11(self):
        """It should evaluate prime"""
        actual = is_prime(11)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_13(self):
        """It should evaluate prime"""
        actual = is_prime(13)
        expected = "prime"
        self.assertEqual(actual, expected)

    def test_negative(self):
        """It should evaluate not prime"""
        actual = is_prime(-1)
        expected = "not prime"
        self.assertEqual(actual, expected)

    def test_not_integer(self):
        """It should evaluate not prime"""
        actual = is_prime(1.5)
        expected = "invalid input"
        self.assertEqual(actual, expected)
