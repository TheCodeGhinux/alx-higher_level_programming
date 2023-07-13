#!/usr/bin/python3
"""
Json python object module
"""
import json


def from_json_string(my_str):
    """
     returns the object representation of a string
    args:
        my_str: string to convert
    return:
        object, else -1 on error
    """
    return json.loads(my_str)
