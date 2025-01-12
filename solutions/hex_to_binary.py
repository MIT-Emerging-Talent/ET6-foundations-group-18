"""
This module provides a utility function to convert a hexadecimal string
to its binary representation.

Functions:
- hex_to_binary: Converts a hexadecimal string to its binary equivalent.

Author: Marc Darazi
"""


def hex_to_binary(hex_string):
    """
    Convert a hexadecimal string to its binary representation.

    Parameters:
        hex_string (str): A string representing a hexadecimal number.
        It can include a leading '0x' prefix or not.

    Returns:
        str: A binary string representation of the given hexadecimal number,
        with leading zeros preserved.

    Raises:
        ValueError: If the input string is not a valid hexadecimal number.

    Example:
        >>> hex_to_binary("1A")
        '11010'
        >>> hex_to_binary("0xFF")
        '11111111'
        >>> hex_to_binary("0x0")
        '0'
    """
    # Remove '0x' prefix if present
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]

    try:
        # Convert to integer, then to binary
        binary_string = bin(int(hex_string, 16))[2:]  # Remove '0b' prefix
        return binary_string
    except ValueError:
        raise ValueError("Invalid hexadecimal string")
