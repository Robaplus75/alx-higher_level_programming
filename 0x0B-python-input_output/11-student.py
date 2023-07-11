#!/usr/bin/python3
"""class student func is defined here"""


class Student:
    """class student representation"""

    def __init__(self, first_name, last_name, age):
        """new student construcotr"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary represetnation"""
        if (all(type(sulu) == str for sulu in attrs) and type(attrs) == list):
            return {num: getattr(self, num) for num in attrs if hasattr(self, num)}
        return self.__dict__

    def reload_from_json(self, json):
        """for replacing attributes of student"""
        for xx, yy in json.items():
            setattr(self, xx, yy)
