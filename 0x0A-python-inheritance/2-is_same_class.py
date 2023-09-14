#!/usr/bin/python3
"""For class-checking"""


def is_same_class(obj, a_class):
    """Check if an object is the same"""
    if type(obj) == a_class:
        return True
    return False
