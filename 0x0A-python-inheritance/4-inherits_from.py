#!/usr/bin/python3
"""Defining an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checking for inherited instance of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
