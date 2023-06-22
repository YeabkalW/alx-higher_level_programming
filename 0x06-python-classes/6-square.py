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

    def __init__(self, size=0, position=(0, 0)):
        """
            sets the attribute of the class
            upon instantiation

            Upon instantiation:
                private attribute set to default
                value

            Args:
                size: size of the square
                Position: postion of whitespace

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

        if isinstance(position, tuple) and len(position) == 2 and \
                all(isinstance(i, int) and i >= 0 for i in position):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
            Use:
                is a public class method that calulate
                area of a square

            Args:
                None

            Returns:
                area of a square
                self.__size ** 2
        """

        return self.__size ** 2

    @property
    def size(self):
        """
        retrives the value of private attribute and
        returns

        Returns:
            Private attribute - __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Updates private instance

            Function:
                set __size to the value inside value
                if the value passes the criteria

            Args:
                value:- the update parameter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        retrives the value of private attribute and
        returns

        Returns:
            Private attribute - __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Updates private instance

            Function:
                set __size to the value inside value
                if the value passes the criteria

            Args:
                value:- the update parameter
        """
        if isinstance(value, tuple) and len(value) == 2 and \
                all(isinstance(i, int) and i >= 0 for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 \
            positive integers")

    def my_print(self):
        """ Prints a square using '#' based on the current
            size of the square

            Returns:
                square made up of #

            example:
                size = 3

                output:
                    ###
                    ###
                    ###
        """

        if self.__size == 0:
            print()
            return

        for row in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(' ' * self.__position[0], end=(""))
            for j in range(self.__size):
                print('#', end="")
            print()
