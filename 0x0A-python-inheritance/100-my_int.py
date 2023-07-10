#!/usr/bin/python3
"""Defines myint class and inherits int"""


class MyInt(int):
    """Inverts int operators"""
    def __ne__(self, value):
        """for overriding != operatrot with =="""
        return self.real == value

    def __eq__(self, value):
        """for overridint the == opeerator  with !="""
        return self.real != value
