#!/usr/bin/python3
"""Inheritance class-checking"""


def is_kind_of_class(obj, a_class):
    """An instance of the parent class"""
    if isinstance(obj, a_class):
        return True
    return False
