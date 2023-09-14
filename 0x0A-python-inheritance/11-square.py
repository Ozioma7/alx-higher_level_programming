#!/usr/bin/python3
"""Defining a class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square"""

    def __init__(self, size):
        """Intialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """The area"""
        return (2 * self.__size)

    def __str__(self):
        """The print() and str() representation of a square."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
