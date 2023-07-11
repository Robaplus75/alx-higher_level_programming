#!/usr/bin/python3
"""Defines a fucntion that converts Json string to python ds"""
import json


def from_json_string(my_str):
    """Returns a python ds object."""
    return json.loads(my_str)
