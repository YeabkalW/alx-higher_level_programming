#!/usr/bin/python3

"""Defines a function that appends
    to a file"""


def append_write(filename="", text=""):
    """a function that appends to the last
    line of a text file

    if the file doesn't exist to will be
    created

    Args:
        filename : the file that a text is added to
        text : the string type line to be added.
    """

    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
