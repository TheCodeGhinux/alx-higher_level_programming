#!/usr/bin/python3
"""
  Function that defines an object
  attribute lookup.
"""


def lookup(obj):
    """This returns a list of
        an object's available attributes.
    """
    return (dir(obj))
