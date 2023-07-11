#!/usr/bin/python3
"""Defines a fucntion that wrties an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves obj test to file"""
    with open(filename, 'w', encoding='utf-8') as myf:
        json.dump(my_obj, myf)
