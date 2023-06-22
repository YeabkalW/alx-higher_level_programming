#!/usr/bin/python3
"""Defines a functiont that checks
    if an object is an instance of a
    a class or a subclass"""


def is_kind_of_class(obj, a_class):
    """checks whether an object is
        instace of a class or its
        subclass
    Args:
        obj - an object
        a_class - a class
    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
