#!/usr/bin/python3

"""defines a method that attribute to
    an object"""

def add_attribute(obje, name, value):
    """checks whether we could add
        attribute to an object. and
        if we could adds it"""

    if hasattr(obje, '__dict__'):
        obje.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
