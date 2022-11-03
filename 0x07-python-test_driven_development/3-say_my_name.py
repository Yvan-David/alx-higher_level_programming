#!/usr/bin/python3
"""
prints names
"""


def say_my_name(first_name, last_name=""):
    """
    prints names
    """
    if (type(first_name) != str):
        raise TypeError('first_name must be a string')
    if (type(last_name) != str):
        raise TypeError('last_name must be a string')
    if (type(first_name) is str and type(last_name) is str):
        print("My name is {} {}".format(first_name, last_name))
