#!/usr/bin/python3
"""square-printing func"""


def print_square(size):
    """Print a square"""

    #raise error if size is not int
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    #raise error if size if negative
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
