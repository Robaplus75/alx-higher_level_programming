#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    newdic = a_dictionary
    if key in a_dictionary:
        del newdic[key]
    return newdic
