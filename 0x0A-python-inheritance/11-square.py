#!/usr/bin/python3

"""defines a class square which
    inherits rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defination of a class Square that
        inherits the Rectangle class to
        share its properties which it self
        inherits BaseGeometry class."""

    def __init__(self, size):
        """creates the objects attribute upon
            creation."""
        Rectangle.__init__(self, size, size)
        self.__size = self.integer_validator("size", size)

    def area(self):
        """calculate the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """prints information about the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
