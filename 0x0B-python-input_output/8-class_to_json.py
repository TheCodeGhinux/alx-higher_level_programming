#!/usr/bin/python3
"""
Class to JSON module
"""


def class_to_json(obj):
    """function that returns the dictionary
    description with simple data structure
    args:
        obj: object
    return:
        serialized object
    """
    return vars(obj)
