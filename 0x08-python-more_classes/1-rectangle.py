#!/usr/bin/python3
"""Defining a Rectangle"""


class Rectangle:
    """Representing a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting/Setting the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isdigit(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting/Setting the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isdigit(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
