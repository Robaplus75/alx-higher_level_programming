#!/usr/bin/python3
""" defines the read_file function"""


def read_file(filename=""):
    """opens the file and prints it's content"""
    with open(filename, 'r', encoding='utf-8') as myf:
        text = myf.read()
    print(text, end="")
