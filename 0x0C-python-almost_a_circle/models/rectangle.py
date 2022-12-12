#!/usr/bin/python3
"""
module for getters and setters
"""
from models.base import Base


class Rectangle(Base):
    """
    class for getters and setters
    """
    def __init__(self, width, heigth, x=0, y=0, id=None):
        """
        method
        """
        super().__init__(id)
        self.__width = width
        self.__heigth = heigth
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        method
        """
        return (self.__width)

    @width.setter
    def width(self, width):
        """
        method
        """
        self.__width = width

    @property
    def x(self):
        """
        method
        """
        return (self.__x)

    @x.setter
    def x(self, x):
        """
        method
        """
        self.__x = x

    @property
    def y(self):
        """
        method
        """
        return (self.__y)

    @y.setter
    def y(self, y):
        """
        method
        """
        self.__y = y

    @property
    def heigth(self):
        """
        method
        """
        return (self.__heigth)

    @heigth.setter
    def heigth(self, heigth):
        """
        method
        """
        self.__heigth = heigth
