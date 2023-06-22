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

    def __init__(self, size=0):
        """
            sets the attribute of the class
            upon instantiation

            Upon instantiation:
                private attribute set to default
                value

            Function:
                it checks the attribute value
                through an if statement and
                raises an error if it fails the
                checks or sets the value if it
                passes
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
