#!/usr/bin/python3
"""Adds two integers together"""


def add_integer(a, b=98):
    """Takes two integers and adds them

    If the arguments are float they are
    casted to integer.

    Exception:
        if the arguments are not either integers or float
        datatype a TypeError exception is raised.
    Args:
        A and B they must be integers
    Returns:
        the sum of two integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
