"""
This module calculates the factorial of a positive number.
We define the factorial of a positive number as the product of all positive integer,
that are less than or equal to the number. 
For example, factorials(5)=5*4*3*2*1=120
"""
def factorials(n: int)->int:
    """
    Calculates the facotrial of non-negative integer.
    The argument, n, is a non-negative integer.
    We choose (0<=n<=100). 
    Returns:
    int, which is the factorials if the number.
    Raises:
    ValueError, if input is non-negative integer, or exceed max. value.
    
    Examples:
    >>> factorials(4)
    24
    >>> factorials(0)
    1
    """
    
    if not isinstance(n, int):
        raise ValueError('input must be an integer')
    
    if n<0:
        raise ValueError('input must be a non-negative integer')
    
    if n>100:
        raise ValueError('Input must not exceed 100')
    
    # We shall use recursion. the base case is factorial of 0 or 1.
    
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorials(n-1)