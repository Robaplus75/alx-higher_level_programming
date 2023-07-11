#!/usr/bin/python3
"""Defines a class to JSON func"""


def class_to_json(obj):
    """Returns dictionary represntation of data structure given."""
    return obj.__dict__
