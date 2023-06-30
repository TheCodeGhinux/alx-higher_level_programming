#!/usr/bin/python3
"Square class"


class Square:
    """Initialize a Square object with a given size.

        Args:
            size (int): The size of the square (default: 0).
    """
    def __init__(self, size=0):
        "Get the size of the square."
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
