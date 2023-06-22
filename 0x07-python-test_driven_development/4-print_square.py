#!/usr/bin/python3
""" a function that prints a square with the character #."""


def print_square(size):
    """prints a square using the
    '#' sybole using the size arg
    as a size parameter to control
    its hieght

    Parameters:

        size must be an integer

        if size is less than 0, raise a ValueError
        exception with the message size must be >= 0

        if size is a float and is less than 0, raise
        a TypeError exception with the message size
        must be an integer

    Args:
        size - used to control size of rows
    Prints:
        A Square

    """

    if not isinstance(size, int):
      raise TypeError('size must be an integer')
    elif size < 0:
      raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
      raise TypeError('size must be an integer')
    else:
      for i in range(size):
        for j in range(size):
          print('#', end=(''))
        print()
