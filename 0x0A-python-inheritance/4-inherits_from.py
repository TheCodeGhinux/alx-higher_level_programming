#!/usr/bin/python3
"""
  Function for
  inherited class-checking function
"""


def inherits_from(obj, a_class):
    """Func that checks if an object is
    an inherited instance of a class.

    Returns:
        True - If obj is an inherited instance of a_class.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
