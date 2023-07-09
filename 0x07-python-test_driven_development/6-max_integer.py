#!/usr/bin/python3
"""For findin max integer in the list"""


def max_integer(list=[]):
    """ If list is empty function returns None"""
    if len(list) == 0:
        return None

    output = list[0]
    num = 1
    #The loop begins
    while num < len(list):
        if list[num] > output:
            output = list[num]
        num += 1
    return output
