#!/usr/bin/python3

"""defines a function that save a JSON
representation of an object in a text file"""

import json


def save_to_json_file(my_obj, filename):
    """converts an object to a JSON file
    and saves it to a text file.

    Args:
        my_obj: python object to be converted to json
        filename: name of file where JSON string is stored"""

    j_str = json.dumps(my_obj)
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(j_str)
