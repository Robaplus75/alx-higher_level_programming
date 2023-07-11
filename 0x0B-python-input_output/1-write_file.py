#!/usr/bin/python3
"""Defines the write file function """


def write_file(filename="", text=""):
    """writes a string to a text file."""
    with open(filename, 'w', encoding='utf-8') as myf:
        return myf.write(text)
