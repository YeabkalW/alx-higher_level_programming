#!/usr/bin/python3

"""defines function that returns a list of list of integers
    representing the Pascals triangle of n"""

def pascal_triangle(n):
    """is a function that returns a list of list that represent
    the pascal triangle of n

    Args:
        n: a number to whom pascal triangle is calculated for."""

    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
