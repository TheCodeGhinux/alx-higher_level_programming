#!/usr/bin/python3
"""
  A class Rectangle that inherits
  from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """
    A class representing a rectangle.

    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Intialize a Rectangle.

        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
