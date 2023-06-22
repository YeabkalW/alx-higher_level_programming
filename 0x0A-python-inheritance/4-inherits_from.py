#!/usr/bin/python3

"""defines a function that check
    if an object is instance of
    a class that inherited directly
    from a specified class"""


def inherits_from(obj, a_class):
    """function that check
        if an object is instance of
        a class that inherited directly
        from a specified class
    Args:
        obj, a_class
    """

    if isinstance(obj, a_class) and issubclass(type(obj), a_class)\
            and type(obj) != a_class:
        return True
    else:
        return False
