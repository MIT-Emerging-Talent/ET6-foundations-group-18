#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

A module gives a summation of two numbers.

@author: Tagwa Hashim
"""


def sum_of(num1, num2):
    """
    Adds two numbers and returns their sum.

    Args:
        num1: The first number. Can be an integer or a float.
        num2: The second number. Can be an integer or a float.

    Returns:
        The sum of num1 and num2.

    Raises:
        AssertionError: If either num1 or num2 is not a number (int or float).

    Examples:
        >>> sum_of(3, 5)
        8
        >>> sum_of(2.5, 3.7)
        6.2
        >>> sum_of("hello", 2.718)
        Traceback (most recent call last):
             ...
        AssertionError: Both arguments must be numbers (int or float).
    """
    assert isinstance(num1, (int, float)) and isinstance(num2, (int, float)), (
        "Both arguments must be numbers (int or float)."
    )
    return num1 + num2
