#!/usr/bin/python3
"""defines a function that turns a
class to a json object"""


def class_to_json(obj):
    """converts a python class
    instance to a json string
    well it attributes.

    Returns:
        a dictionary that is ready for serialization.
    """

    obj_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[key] = value

    return obj_dict
