#!/usr/bin/python3
"""A text reading function defination"""


def read_file(filename=""):
    """Reading a file"""
    with open(filename, encoding="utf-8") as f:
        f.read()
