#!/usr/bin/python3
"""
Create object from a JSON file module
"""
import json


def load_from_json_file(filename):
    """
     function that creates an Object from a JSON file
    args:
        filename: text file
    return:
        object, else -1 on error
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
