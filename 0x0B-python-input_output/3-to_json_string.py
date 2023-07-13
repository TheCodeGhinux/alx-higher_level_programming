#!/usr/bin/python3
"""
Function that coverts json
a string.
"""
import json


def to_json_string(my_obj):
    """
     returns the JSON representation
     of an object (string):
    args:
        my_obj: object to convert
    return:
        object, else -1 on error
    """
    return json.dumps(my_obj)
