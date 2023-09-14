#!/usr/bin/python3
"""Defining MyInt class"""


class MyInt(int):
    """!= and == inverter"""

    def __eq__(self, value):
        """!= overiding =="""
        return self.real != value

    def __ne__(self, value):
        """== overriding !="""
        return self.real == value
