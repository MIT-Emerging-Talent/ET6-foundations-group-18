#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the maximum number of a list of numbers.

@author: Tagwa Hashim
"""


def max_in(numbers):
    """
    Finds the maximum number in a list of numbers

    Args:
      numbers: A list of numbers (integers or floats).

    Returns:
      The maximum number in the list.

    Raises:
      ValueError: If the input is not a list.
      ValueError: If the input list is empty.
      TypeError: If the list contains non-numeric elements.

    Examples:
      >>> max_in([1, 5, 3, 9, 2])
      9
      >>> max_in([2.5, 1.02, 5.7])
      5.7
      >>> max_in([10.5, -5.2, 8])
      10.5
      >>> max_in([1, -5, -3])
      1
      >>> max_in([])
      Traceback (most recent call last):
      ValueError: List cannot be empty.
      >>> max_in("not a list")
      Traceback (most recent call last):
      ValueError: Input must be a list.
      >>> max_in([1, 2, "three"])
      Traceback (most recent call last):
      TypeError: List contains non-numeric elements.
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if not numbers:
        raise ValueError("List cannot be empty.")
    for num in numbers:
        if not isinstance(num, (int, float)):  # Check if any element is not numeric
            raise TypeError("List contains non-numeric elements.")

    max_num = numbers[0]  # Initialize max_num with the first element

    for num in numbers[1:]:  # Iterate through the list starting from the second element
        if num > max_num:
            max_num = num

    return max_num
