#!/usr/bin/python3

"""A class the defines a Rectangle"""


class Rectangle:
    """a class that sets the template
        to definig an actual rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the width and height of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """prints a rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rec = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    try:
                        rec += str(self.print_symbol)
                    except Exception:
                        rec += type(self).print_symbol
                if i < self.__height - 1:
                    rec += '\n'
            return rec

    def __repr__(self):
        """returns a string that enables recreation of
            instace using the eval"""
        return "Rectangle(2, 4)"

    def __del__(self):
        """returns a deleation message when an instance
            is deleted."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rec_1, rec_2):
        """compares a rectangle"""
        if not isinstance(rec_1, Rectangle):
            raise TypeError('rec_1 must be an instance of Rectangle')
        elif not isinstance(rec_2, Rectangle):
            raise TypeError('rec_2 must be an instance of Rectangle')
        elif rec_1.area == rec_2.area:
            return rec_1

        if rec_1.area() > rec_2.area():
            return rec_1
        else:
            return rec_2

    @classmethod
    def square(cls, size=0):
        """Alternative constructor"""
        return cls(size, size)
