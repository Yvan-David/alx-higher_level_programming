#!/usr/bin/python3
"""
module for file writting
"""


def write_file(filename="", text=""):
    """
    method for file writing
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
