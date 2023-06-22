#!/usr/bin/python3

"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ divides elements of a matrixs

    it divides elements of a matrix if
    they are either an integer or float
    data type if not it raises a type error
    exception.

    and rows of matrix must be of equal size
    further more each element must be divisable
    by "Div".

    Args:
        a matrix: that should be made up of ints and
                floats.
        A div: a number which each element of the matrix
                should be divided with

    Returns:
        A new matrix : where each element is rounded up to
                    2 decimal place
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of list) of" \
                                " integers/floats")

    return [[round(j/div, 2) for j in i] for i in matrix]
