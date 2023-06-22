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
            raises an exceprion that notifies
            about the status of the area()"""
        raise Exception('area() is not implemented')
