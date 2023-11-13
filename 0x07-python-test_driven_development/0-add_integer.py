#!/usr/bin/python3
"""Sum of two integers"""


def add_integer(a, b=98):
    """adds two integers then returns the result
    a, b are typecasted to ints if they were floats else raises TypeError
    Args:
          a (int): first integer
          b (int): second integer
    Returns:
        addition of a and b
    Raises:
        TypeError: a must be an integer or b must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
