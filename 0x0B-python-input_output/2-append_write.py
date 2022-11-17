#!/usr/bin/python3
"""
module for file appending
"""


def append_write(filename="", text=""):
    """
    method for file appending
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
