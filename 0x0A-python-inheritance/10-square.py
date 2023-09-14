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
        return self.__size ** 2
