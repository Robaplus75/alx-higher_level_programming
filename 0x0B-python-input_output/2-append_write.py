#!/usr/bin/python3
"""Define append write function"""


def append_write(filename="", text=""):
    """Appends text to the file"""
    with open(filename, 'a', encoding='utf-8') as myf:
        return myf.write(text)
