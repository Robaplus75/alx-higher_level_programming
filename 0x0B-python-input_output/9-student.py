#!/usr/bin/python3
"""a class studen func is defined here"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """New student constructor."""
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self):
        """return dictionary representation"""
        return self.__dict__
