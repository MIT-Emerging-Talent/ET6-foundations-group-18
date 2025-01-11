"""
Module: Binary to Hexadecimal Converter

This module provides a utility function to convert binary strings to their
corresponding hexadecimal representations. It validates the input to ensure
that it contains only binary digits (0s and 1s) and performs the conversion
accurately.

@author: Marc Darazi
"""


def binary_to_hex(binary_str):
    """
    Convert a binary string to its hexadecimal representation.

    Parameters:
        binary_str (str): A string of 0s and 1s representing a binary number.

    Returns:
        str: The hexadecimal representation of the binary number.

    Raises:
        ValueError: If the input is not a valid binary string.

    Example:
        >>> binary_to_hex("1101")
        'D'
        >>> binary_to_hex("11110000")
        'F0'
        >>> binary_to_hex("101010101010")
        'AAA'
    """
    # Validate input
    if not all(char in "01" for char in binary_str):
        raise ValueError("Input must be a binary string containing only 0s and 1s.")

    # Convert binary string to integer
    decimal_value = int(binary_str, 2)

    # Convert integer to hexadecimal string and return
    return hex(decimal_value)[2:].upper()
