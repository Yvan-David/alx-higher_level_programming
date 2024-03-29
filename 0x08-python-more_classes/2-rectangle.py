#!/usr/bin/python3
"""
class called rectangle
"""


class Rectangle():
    """
    class called rectangle
    """
    def __init__(self, width=0, height=0):
        """
        class called rectangle
        """

        if (type(width) == int) and (width >= 0):
            self.__width = width
        if (type(height) == int) and (height >= 0):
            self.__height = height
        if (type(width) != int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if (type(height) != int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width != 0 and self.__height != 0):
            return ((2 * self.__height) + (2 * self.__width))
        else:
            return (0)
