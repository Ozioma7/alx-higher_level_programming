#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Representing a square"""
    def __init__(self, size):
        """Initialization
        Args:
            size (int):
        """
        self.size = size

    @property
    def size(self):
        """Getting a setting the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Getting a setting the size of the square"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
