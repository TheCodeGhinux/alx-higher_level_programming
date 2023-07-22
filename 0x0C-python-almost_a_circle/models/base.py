#!/usr/bin/python3
"""Base class."""
import turtle
import json
import csv


class Base:
    """Defines a base model.

    Defines the "base" for all other classes in
    project 0x0C-python-almost_a_circle.

    Attributes:
        __nb_objects (int): Instantiated Bases number.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Defines a new Base.

        Args:
            id (int): New base identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries: A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization of a list of objects.

        Args:
            list_objs: List of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    f_name = ["id", "width", "height", "x", "y"]
                else:
                    f_name = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, f_name=f_name)
                for items in list_objs:
                    writer.writerow(items.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes from a CSV file.

        Returns:
            a list of instantiated classes.
            Otherwise - an empty list.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    f_name = ["id", "width", "height", "x", "y"]
                else:
                    f_name = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, f_name=f_name)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares with turtle.

        Args:
            list_rectangles (list): Rectangle List.
            list_squares (list): Square List.
        """
        rect = turtle.Turtle()
        rect.screen.bgcolor("#b7312c")
        rect.pensize(3)
        rect.shape("turtle")

        rect.color("#ffffff")
        for rect in list_rectangles:
            rect.showturtle()
            rect.up()
            rect.goto(rect.x, rect.y)
            rect.down()
            for i in range(2):
                rect.forward(rect.width)
                rect.left(90)
                rect.forward(rect.height)
                rect.left(90)
            rect.hideturtle()

        rect.color("#b5e3d8")
        for sq in list_squares:
            rect.showturtle()
            rect.up()
            rect.goto(sq.x, sq.y)
            rect.down()
            for i in range(2):
                rect.forward(sq.width)
                rect.left(90)
                rect.forward(sq.height)
                rect.left(90)
            rect.hideturtle()

        turtle.exitonclick()
