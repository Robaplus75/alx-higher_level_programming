#!/usr/bin/python3
"""Defines is kind of class fucntion"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance or inherited."""
    if isinstance(obj, a_class):
        return True
    return False
