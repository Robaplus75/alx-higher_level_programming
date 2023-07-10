#!/usr/bin/python3
"""defines inherits ffrom function"""


def inherits_from(obj, a_class):
    """for checking if the object is inherited instance or not"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    k = False
    return k
