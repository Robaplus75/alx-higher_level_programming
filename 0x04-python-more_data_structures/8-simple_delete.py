#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    newdic = a_dictionary
    del newdic[key]
    return newdic
