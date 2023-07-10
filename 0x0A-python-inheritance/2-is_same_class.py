#!/usr/bin/python3
"""Define is same class function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class
    """
    if a_class == type(obj):
        return True
    return False
