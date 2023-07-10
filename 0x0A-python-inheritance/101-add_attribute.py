#!/usr/bin/python3
"""Defines an add attribut function"""


def add_attribute(obj, att, value):
    """Adds new attributes to the object if it can """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    # setattr function called
    setattr(obj, att, value)
