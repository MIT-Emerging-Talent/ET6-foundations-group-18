"""
Module: Binary to Hexadecimal Converter

This module provides a utility function to convert binary strings to their 
corresponding hexadecimal representations. It validates the input to ensure 
that it contains only binary digits (0s and 1s) and performs the conversion 
accurately.

Functions:
    - binary_to_hex(binary_str): Converts a binary string to its hexadecimal representation.

Usage Example:
    >>> from binary_to_hex import binary_to_hex
    >>> binary_to_hex("1101")
    'D'

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
    """
    # Validate input
    if not all(char in '01' for char in binary_str):
        raise ValueError("Input must be a binary string containing only 0s and 1s.")

    # Convert binary string to integer
    decimal_value = int(binary_str, 2)

    # Convert integer to hexadecimal string and return
    return hex(decimal_value)[2:].upper()

# Unit Tests
def test_binary_to_hex_valid():
    """
    Test binary_to_hex with valid binary input.
    Asserts the correct hexadecimal output is produced.
    """
    assert binary_to_hex("1101") == "D"

def test_binary_to_hex_large():
    """
    Test binary_to_hex with a larger binary input.
    Asserts the correct hexadecimal output is produced.
    """
    assert binary_to_hex("11110000") == "F0"

def test_binary_to_hex_minimum():
    """
    Test binary_to_hex with the smallest valid binary input.
    Asserts the correct hexadecimal output is produced.
    """
    assert binary_to_hex("0") == "0"

def test_binary_to_hex_invalid():
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
