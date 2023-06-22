#!/usr/bin/python3

"""Defines a function that retrives and
    returns a list of all methods and
    attributes that are present in a class
"""


def lookup(obj):
    """gets all avaliable attribute and
        methods of a class objects and
        returns a list of them

    Args:
        Obj - class object

    Returns:
        a new list containing all attributes
        and methods of arg passed"""
    return dir(obj)
