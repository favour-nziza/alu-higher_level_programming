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
    if ((not isinstance(a, int) and not isinstance(a, float))
            or isinstance(a, bool)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))
            or isinstance(b, bool)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
