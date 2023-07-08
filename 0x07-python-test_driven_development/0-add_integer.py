#!/usr/bin/python3

"""Module for integers addition task"""


def add_integer(a, b=98):

    """ Adds two integers """

    if type(a) == float:
        a = int(a)
    elif type(a) == int:
        pass
    else:
        raise TypeError("a must be an integer")

    if type(b) == float:
        b = int(b)
    elif type(b) == int:
        pass
    else:
        raise TypeError("b must be an integer")
    return a + b
