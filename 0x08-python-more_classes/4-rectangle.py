#!/usr/bin/python3
"""Eval is magic."""


class Rectangle:
    """Defines a class of Rectangle."""

    def __init__(self, width=0, height=0):
        """Defines and initialize a new Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines and sets Rectangle width."""
        return self.rec_width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.rec_width = value

    @property
    def height(self):
        """Defines and sets Rectangle height."""
        return self.rec_height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.rec_height = value

    def area(self):
        """Defines and return the area of the Rectangle."""
        return (self.rec_width * self.rec_height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.rec_width == 0 or self.rec_height == 0:
            return (0)
        return ((self.rec_width * 2) + (self.rec_height * 2))

    def __str__(self):
        """Defines and returns the printable
        representation of the Rectangle.
        """
        if self.rec_width == 0 or self.rec_height == 0:
            return ("")

        shape = []
        for i in range(self.rec_height):
            [shape.append('#')
             for j in range(self.rec_width)]
            if i != self.rec_height - 1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """Defines and returns the string
        representation of the Rectangle."""
        shape = "Rectangle(" + str(self.rec_width)
        shape += ", " + str(self.rec_height) + ")"
        return (shape)
