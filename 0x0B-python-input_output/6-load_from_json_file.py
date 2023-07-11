#!/usr/bin/python3
"""Defines a fucntion that creates an object form a json file"""
import json


def load_from_json_file(filename):
    """Loads json from a file."""
    with open(filename) as myf:
        return json.load(myf)
