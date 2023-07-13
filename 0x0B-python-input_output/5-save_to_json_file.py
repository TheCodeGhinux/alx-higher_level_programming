#!/usr/bin/python3
"""
Save oject to file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
     function that writes an Object
     to a text file, using a JSON representation
    args:
        my_obj: object to manipulate
    filename:
        filename: text file
    return:
        object, else -1 on error
    """
    with open(filename, "w", encoding="utf-8") as f:
        written = json.dump(my_obj, f)
    return written
