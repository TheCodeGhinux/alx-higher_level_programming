#!/usr/bin/python3
"""
Student to disk and reload Module
"""


class Student:
    """
    A class that defines a Student
    """

    def __init__(self, first_name, last_name, age):
        """initialize the method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of student instance
        args:
            attrs: attributes
        return:
            na
        """
        if not attrs:
            return vars(self)

        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})

    def reload_from_json(self, json):
        """replace attributes method
        args:
            json: json object
        return:
            na
        """
        self.__dict__.update(json)
