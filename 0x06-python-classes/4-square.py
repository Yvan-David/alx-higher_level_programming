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

    @property
    def size(self):
        if (type(self.__size) == str):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            return (self.__size)

    @size.setter
    def size(self, value):
        if (type(self.__size) is str):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        if (type(self.__size) is str):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            return (self.__size ** 2)
