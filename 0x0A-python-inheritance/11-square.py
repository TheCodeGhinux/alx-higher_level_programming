#!/usr/bin/python3
"""
  A class of Square that inherits
  from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Func representation of a square."""

    def __init__(self, size):
        """Init new square.

        Args:
            size (int): Size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
