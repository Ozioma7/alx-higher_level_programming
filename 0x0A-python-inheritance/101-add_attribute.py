#!/usr/bin/python3
"""Defining add_attribute class"""


def add_attribute(obj, att, value):
    """Adding a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
