#!/usr/bin/python3
"""Defining a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization"""
	super().integer_validator("width", width)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """The print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
