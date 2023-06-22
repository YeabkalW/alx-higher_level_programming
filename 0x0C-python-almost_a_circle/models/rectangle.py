#!/usr/bin/python3
"""defines a class that inherits from the Base class
named rectangle"""

from models.base import Base


class Rectangle(Base):
    """a class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class up on instance creation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrives the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private attribute width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Retrives the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the private attribute height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrives the private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the private attribute x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrives the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the private attibute y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """claculates the area of a rectangle using widht and height"""
        area = self.__width * self.__height
        return area

    def display(self):
        """Prints to the stdout a rectangle made up of '#' characters"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for g in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end=(""))
            print()

    def __str__(self):
        """defines a string to be display when print is called"""
        return "[{}] ({}) {}/{} - {}/{}"\
               .format(type(self).__name__, self.id, self.__x, self.__y,
                       self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update the values of attributes"""

        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns the dictionary representation of Self"""
        return {
            'x': int(getattr(self, "x")),
            'y': getattr(self, "y"),
            'id': getattr(self, "id"),
            'width': getattr(self, "width"),
            'height': getattr(self, "height")
        }
