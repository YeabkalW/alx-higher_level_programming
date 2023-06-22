#!/usr/bin/python3

"""defines a class that inherits
    BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a recrtangle and
        inherits properties of BaseGeometry"""

    def __init__(self, width, height):
        """initalizes the Rectangel class
            upon creation of an object"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
