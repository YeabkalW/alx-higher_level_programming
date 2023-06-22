#!/usr/bin/python3

"""A class the defines a Rectangle"""


class Rectangle:
    """a class that sets the template
        to definig an actual rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the width and height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns private attribute __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value to the private attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """returns private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value to the private attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
