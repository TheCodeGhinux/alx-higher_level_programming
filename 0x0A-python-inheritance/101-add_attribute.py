#!/usr/bin/python3
"""
  Function that
  adds attributes to objects.
"""


def add_attribute(obj, att, value):
    """Add new attribute to an object.

    Raises:
        TypeError: When attribute added fails.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
