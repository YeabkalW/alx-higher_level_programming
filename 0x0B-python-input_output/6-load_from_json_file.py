#!/usr/bin/python3

"""Defines a function that
creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creats an object from a JSON object
    and .json file

    Args:
        filename: json file name"""

    with open(filename, encoding="UTF-8") as f:
        ob_j = json.loads(f.read())
    return ob_j
