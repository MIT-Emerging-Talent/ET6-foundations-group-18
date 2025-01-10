#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The module checks whether a given year is a leap year.
create by Muna Sattouf on January 9, 2025
Completed on January 10, 2024

A year is a leap year if it is divisible by 4,
and if it is divisible by 100, it must also be divisible by 400.
"""

def leap_year(year: int) -> bool:
    """
    Checks whether the given year is a leap year.
    
    Argument:
    year, a positive integer
    
    Returns:
    boolean: True if the year is a leap year, false otherwise.
    
    Examples: 
    >>> leap_year(2024)
    True
    >>> leap_year(1900)
    False
    >>> leap_year(2021)
    False
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    if year < 0:
        raise ValueError("Year must be positive integer")
    
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))