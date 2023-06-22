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

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Prints and returns a message"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
