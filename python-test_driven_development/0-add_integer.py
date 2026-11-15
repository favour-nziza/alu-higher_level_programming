#!/usr/bin/python3
"""Defines an integer addition function.

The function add_integer adds two integers or floats (floats are first
cast to integers) and returns the result as an integer.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecast to ints before the addition.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
