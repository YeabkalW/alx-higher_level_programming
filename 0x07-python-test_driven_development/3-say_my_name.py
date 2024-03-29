#!/usr/bin/python3

"""prints name of the
author"""


def say_my_name(first_name, last_name=""):
    """a function that prints the name of
    that is passed to it, checks if the
    arguments are strings if not it raises
    a TypeError.

    Args:
        first_name : first name of user
        last_name : last name of user

    Returns:
        noting

    Print:
        the first and last name of the user
        that was passed to it
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
