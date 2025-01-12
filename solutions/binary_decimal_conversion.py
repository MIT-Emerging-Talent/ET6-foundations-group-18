#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting between binary and decimal numbers.
Created by Muna Sattouf on 29/12/2024
Completed on 1/1/2025
"""


def decimal_to_binary(decimal: int) -> str:
    """
    This function takes a decimal number from command line as paramter,
    and returns its binary representation.

    Example: DecimalToBinary('binary', 392)
    >>> 110001000

    """

    if not isinstance(decimal, int):
        raise ValueError
    """
    Input must be an integer
    """
    if decimal < 0:
        decimal = -decimal
        return "-" + decimal_to_binary(decimal)
    if decimal == 0:
        return "0"
    binarynumber = ""
    while decimal > 0:
        binarynumber = str(decimal % 2) + binarynumber
        decimal = decimal // 2
    return binarynumber


def binary_to_decimal(binary: str) -> int:
    """
    This function takes a binary number from command line as paramter,
    and returns its decimal representation.

    Example: binary_to_decimal('decimal', 10011101)
    >>> 157

    Example: binary_to_decimal('decimal', 'hello')
    >>> ValueError: Input must only contain 0s and 1s
    """
    if not all(c in "01" for c in binary):
        raise ValueError("Input must only contain 0s and 1s")
    decimalnumber = 0
    for c in binary:
        decimalnumber = decimalnumber * 2 + int(c)
    return decimalnumber


def binary_decimal_conversion(conversion_type: str, number: str) -> str:
    """
    This is the main function: It 'coordinates' and decides
    which of the two above functions to use
    """
    if conversion_type == "decimal":
        if not all(c in "01" for c in number):
            raise ValueError(
                "If decimal conversion, input must be in binary, consisting only of 0 and 1"
            )
        return binary_to_decimal(number)
    elif conversion_type == "binary":
        if not number.isdigit():
            raise ValueError("If binary conversion, input must be a positive integer")
        decimal = int(number)
        return decimal_to_binary(decimal)
    else:
        raise ValueError("Conversion Type must be 'binary' or 'decimal ' ")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print(
            "To use properly, the first argument is conversion type. the second is the number you want to convert."
        )
        sys.exit(1)

    conversion_type = sys.argv[1].lower()
    number = sys.argv[2]

    if conversion_type not in ["binary", "decimal"]:
        print("Error: Conversion type must be binary or decimal")
        sys.exit(1)

    if conversion_type == "decimal":
        if not all(c in "01" for c in number):
            print(
                "Error: for decimal conversion, input must be in binary, containing only 1 and 0"
            )
            sys.exit(1)
        result = binary_to_decimal(number)

    elif conversion_type == "binary":
        if not number.isdigit():
            print("Error: for binary conversion, input must be positive integer")
            sys.exit(1)
        result = decimal_to_binary(int(number))
    print(result)
