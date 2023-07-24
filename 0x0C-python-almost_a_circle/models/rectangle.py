#!/usr/bin/python3
""" First Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Defines and init a new Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
            x (int): X coordinate of Rectangle.
            y (int): Y coordinate of Rectangle.
            id (int): id of Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Defines and sets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Defines and sets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Defines and sets the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Defines and sets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines and returns the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints Rectangle with the `#`."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the Rectangle.

        Args:
            *args (ints): New attribute values.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            d = 0
            for arg in args:
                if d == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif d == 1:
                    self.width = arg
                elif d == 2:
                    self.height = arg
                elif d == 3:
                    self.x = arg
                elif d == 4:
                    self.y = arg
                d += 1

        elif kwargs and len(kwargs) != 0:
            for g, h in kwargs.items():
                if g == "id":
                    if h is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = h
                elif g == "width":
                    self.width = h
                elif g == "height":
                    self.height = h
                elif g == "x":
                    self.x = h
                elif g == "y":
                    self.y = h

    def to_dictionary(self):
        """Defines and returns the dictionary repr of Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
