#!/usr/bin/python3
"""Base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsenting base geometry."""

    def area(self):
        """Area not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
