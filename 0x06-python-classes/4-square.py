#!/usr/bin/python3
"Square class"


class Square:
    "Class to represent a Square"

    def __init__(self, size=0):
        """Initialize a Square object with a given size.
        
        Args:
            size (int): The size of the square (default: 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        "Get and returns the size of the square."
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with int value.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        "Calculate and returns the area of the square."
        return self.__size ** 2
