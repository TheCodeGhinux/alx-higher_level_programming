#!/usr/bin/python3
"""
  Function that defines
  class-checking
"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance
    of the specified class.

    Returns:
        True - If obj is exactly an instance of the class
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
