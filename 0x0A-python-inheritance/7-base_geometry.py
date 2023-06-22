#!/usr/bin/python3

"""Defines a class that represents
    Geometry."""


class BaseGeometry(object):
    """a class representing a
        geometry
    Defines:
        a public instance method"""

    def area(self):
        """Pubnce attribulic instate that
            raises an exception that notifies
            about the status of the area()"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value to be integer else
            raises an exception same thing with
            if value is zero
        Args:
            name - string
            value- the number to be validated
        Returns:
            execption msg if parameter are not mate"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
