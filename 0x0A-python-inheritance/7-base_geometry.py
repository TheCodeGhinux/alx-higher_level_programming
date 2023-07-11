#!/usr/bin/python3
"""
  A class of BaseGeometry.
"""


class BaseGeometry:
    """function that defines base geometry."""

    def area(self):
        """function that defines base geometry."""
        raise Exception("area() is not implemented")
        """Defines a base geometry class BaseGeometry."""

    def integer_validator(self, name, value):
        """To validate a parameter as int.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
