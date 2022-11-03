#!/usr/bin/python3
"""
this is a module that has a function adding int
"""


def add_integer(a, b=98):
    """
    this is a function that adds int
    """
    if (type(a) == float):
        a = int(a)
    if (type(b) == float):
        b = int(b)
    if ((type(a) == (int or float)) and (type(b) == (int or float))):
        return (a + b)
    else:
        if (type(a) != int and type(a) != float):
            raise TypeError('a must be an integer')
        if (type(b) != int and type(b) != float):
            raise TypeError('b must be an integer')
