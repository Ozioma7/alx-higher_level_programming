#!/usr/bin/python3
"""Defining a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON rep of a string object."""
    return json.dumps(my_obj)
