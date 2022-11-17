#!/usr/bin/python3
"""
module for file reading
"""


def read_file(filename=""):
    """
    method for file reading
    """
    with open(filename, 'r') as file:
        for lie in file:
            print(lie)
