#!/usr/bin/python3
"""
  Function that
  inherited class-checking function
"""


def is_kind_of_class(obj, a_class):
    """func to check if an object is an
    instance or inherited instance of a class.

    Returns:
         True - If obj is an instance or
         inherited instance of a_class
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
