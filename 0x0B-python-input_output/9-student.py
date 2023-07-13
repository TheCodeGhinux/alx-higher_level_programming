#!/usr/bin/python3
"""
Student Class Module
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

    def to_json(self):
        """
        retrieves a dictionary representation of student instance
        """
        return vars(self)
