#!/usr/bin/python3
"""class student is defined here"""


class Student:
    """student class represetntaion"""

    def __init__(self, first_name, last_name, age):
        """New student constructor """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary represetntation """
        if (all(type(sulu) == str for sulu in attrs) and type(attrs) == list):
            return {num: getattr(self, num) for num in attrs if hasattr(self, num)}
        return self.__dict__
