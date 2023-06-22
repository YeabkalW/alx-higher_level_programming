#!/usr/bin/python3
"""Defines a class that inherits
    the list parent class"""


class MyList(list):
    """a class inheriting the list class
        and defines a instance attribute
        that sorts a list in asscending
        order."""

    def print_sorted(self):
        """prints a list but sorted in
            ascending order
        Prints:
            a list sorted ascending order
        """

        print(sorted(self))
