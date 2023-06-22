#!/usr/bin/python3

"""defines a function that writes a string to
    a text file in UTF-8 encoding.
"""


def write_file(filename="", text=""):
    """A function that write to a text file

    Args:
        filename: a string rep of the file name.
        text: the string to be written on the file.
    """

    with open(filename, mode='w', encoding='UTF-8') as f:
        return f.write(text)
