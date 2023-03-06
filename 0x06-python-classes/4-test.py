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
            try:
                self.size = size
                print(type(self.size))
                if (type(size) != int):
                    raise TypeError("size must be an integer")
                elif (self.size < 0):
                    raise ValueError("size must be >= 0")
            except Exception as e:
                print(e)
    def area(self):
        if ((self.size) == 3):
            raise TypeError("size must be an integer")
        elif (self.size < 0):
            raise ValueError("size must be >= 0")
        else:
            return (self.size ** 2)
