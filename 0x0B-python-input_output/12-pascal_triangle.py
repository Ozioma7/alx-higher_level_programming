#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n"""
    if n <= 0:
        return []
    list = [1]
    for i in list:
        print(list)
        newlist = []
        newlist.append(list[0])
        for i in range(len(list) -1):
            newlist.append(list[i] + list[i + 1])
        newlist.append(list[-1])
        list = newlist
