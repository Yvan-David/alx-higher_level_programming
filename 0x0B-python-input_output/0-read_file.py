#!/usr/bin/python3
"""
module for file reading
"""


def read_file(filename=""):
    """
    method for file reading
    """
    with open(filename, 'r', encoding="utf-8") as file:
        for lie in file:
            print(lie, end='')
