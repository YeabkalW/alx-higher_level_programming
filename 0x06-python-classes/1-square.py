#!/usr/bin/python3

""" Defines a class that defines a square

    Attribute:
        a private atribute that holds the
        size of the square.
"""


class Square:
    """
        A class that holds the size of the
        size of a square and hides it from
        being changed

        Attributes:
            Public:
                None
            Private:
                __size - holds the size of
                         a square hiddenly
    """

    def __init__(self, size):
        """
            sets the attribute of the class
            upon instantiation
        """
        self.__size = size
