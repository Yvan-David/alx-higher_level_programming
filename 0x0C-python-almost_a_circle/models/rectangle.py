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
        i = ['width', 'heigth', 'x', 'y']
        n = [width, heigth, x, y]
        for u in range(3):
            if type(n[u]) is not int:
                raise TypeError(f"{i[u]} must be an integer")
        for v in [width, heigth]:
            for u in range(1):
                if v <= 0:
                    raise ValueError(f"{i[u]} must be > 0")
        for z in [x, y]:
            if x < 0:
                raise ValueError("x must be >= 0")
            if y < 0:
                raise ValueError("y must be >= 0")
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
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
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(heigth) is not int:
            raise TypeError("heigth must be an integer")
        elif heigth <= 0:
            raise ValueError("heigth must be > 0")
        self.__heigth = heigth
