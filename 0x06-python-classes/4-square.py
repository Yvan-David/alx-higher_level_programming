#!/usr/bin/python3
"""this is a module that makes a class."""


class Square:
    """this is a class called square."""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.size = size

    def area(self):
        if (type(self.size) != int):
            raise TypeError("size must be an integer")
        elif (self.size < 0):
            raise ValueError("size must be >= 0")
        else:
            return (self.size ** 2)
