#!/usr/bin/python3

"""
this module defines a rectangle class
which is subclass of base
"""
from models.base import Base


class Rectangle(Base):
    """
    this module defines a rectangle class
    which is subclass of base
    """

    def get_width(self):
        """
        retreives width
        """
        return self.__width

    def set_width(self, width):
        """
        sets width
        """
        self.__width = width

    def get_height(self):
        """
        retreives height
        """
        return self.__height

    def set_height(self, height):
        """
        sets height
        """
        self.__height = height

    def get_x(self):
        """
        retreives x
        """
        return self.__x

    def set_x(self, x):
        """
        sets x
        """
        self.__x = x

    def get_y(self):
        """
        retreives y
        """
        return self.__y

    def set_y(self, y):
        """
        sets y
        """
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
