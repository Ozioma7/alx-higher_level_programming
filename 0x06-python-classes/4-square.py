#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representing a square"""
    def __init__(self, size=0):
        """Initialization
        Args:
            size (int):
        """
        self.size = size

    @property
    def size(self):
        """Getting and setting the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Getting and setting the size of the square"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size ** 2)
