#!/usr/bin/python3

"""Defines a function that converts a JSON
    object to its python data structure form"""

import json


def from_json_string(my_str):
    """converts a JSON string(object)
    back to its python data structure form

    Args:
        my_str: the JSON object to be converted"""
    st_r = json.loads(my_str)
    return st_r
