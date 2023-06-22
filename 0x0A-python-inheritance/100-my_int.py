#!/usr/bin/python3
"""defines a class MyInt the inherits
    Int"""


class MyInt(int):
    """class inheriting integer class"""
    def __eq__(self, other):
        """over rides the == operation"""
        return int(self) != other

    def __ne__(self, other):
        """Over rides the != operator"""
        return int(self) == other
