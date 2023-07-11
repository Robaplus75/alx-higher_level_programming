#!/usr/bin/python3
"""Defines a function that returns a JSON represetnation."""
import json

def to_json_string(my_obj):
    """Returns json represetnation"""
    return json.dumps(my_obj)
