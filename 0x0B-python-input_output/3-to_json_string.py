#!/usr/bin/python3

"""Defines a function that converts python
    data structure to JSON object.
"""
import json


def to_json_string(my_obj):
    """Convert a python object to its JSON
    object representation

    Args:
        my_obj: a python object to be converted
        to a JSON object
    """
    j_son = json.dumps(my_obj)
    return j_son
