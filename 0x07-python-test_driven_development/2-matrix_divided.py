#!/usr/bin/python3
"""
a module of a matrix
"""


def matrix_divided(matrix, div):
    """
    a matrix that divides each elt
    """
    rmatrix = []
    v = len(matrix[0])
    for i in matrix:
        fmatrix = []
        if (type(i) == list):
            if (len(i) == v):
                for n in i:
                    if (type(n) == (int or float)):
                        if (type(div) == (int or float)):
                                if (div != 0):
                                    fmatrix.append(round((n / div),2))
                                else:
                                    raise ZeroDivisionError('division by zero')
                        else:
                            raise TypeError("div must be a number")
                    else:
                        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
                rmatrix.append(fmatrix)
            else:
                raise TypeError('Each row of the matrix must have the same size')
        else:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    return(rmatrix)
