#!/usr/bin/python3
"""Inherited list class MyList."""


class MyList(list):
    """Sorted printing for the built-in list class."""

    def print_sorted(self):
        """Printing a sorte dlist"""
        print(sorted(self))
