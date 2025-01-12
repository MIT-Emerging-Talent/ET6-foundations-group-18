#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for finding if an integer is prime.

Module contents:
    - is_prime: finds if an integer is prime.

Created on XX XX XX
@author: Mohammed Elfadil
"""


def is_prime(a: int) -> str:
    """Checks if an integer is prime.
    Parameter:
        a: int
    Return -> str: whether a is prime or not
    Raises:
        AssertionError: if the argument is not an integer
    >>> is_prime(0)
    not prime
    >>> is_prime(1)
    not prime
    >>> is_prime(2)
    prime
    >>> is_prime(4)
    not prime
    >>> is_prime(7)
    prime
    >>> is_prime(2.5)
    invalid input
    >>> is_prime(-1)
    not prime
    """
    if not isinstance(a, int):
        return "invalid input"
    if a < 2:
        return "not prime"
    for i in range(2, a):
        if a % i == 0:
            return "not prime"
    return "prime"
