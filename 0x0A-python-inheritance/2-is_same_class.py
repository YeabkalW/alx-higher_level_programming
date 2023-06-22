#!/usr/bin/python3
"""Defines a function that checks if
    an instance belongs in specified
    class"""


def is_same_class(obj, a_class):
    """Checks whether an instance
        belongs to passed class

    Args:
        obj :- said object of a class
        a_class :- class to be checked for inst
    Returns:
        True :- if instance is of a_class
        False :- if instace is not of a_class"""

    if type(obj) is a_class:
        return True
    else:
        return False
