#!/usr/bin/python3

"""Defines a function that adds
a specific line after a line containing
a specific word"""


def append_after(filename="", search_string="", new_string=""):
    """appends file after a specific line containg a specific
    word

    Args:
        filename: the file to be openned and modified
        search_string"""

    with open(filename, mode="r+", encoding="UTF-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
