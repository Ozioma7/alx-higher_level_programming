#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representing a Square"""
    def __init__(self, size=0):
        """Initialization
        Args:
            size (int):
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif type(size) < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Return the current area of square"""
        return (self.__size ** 2)
