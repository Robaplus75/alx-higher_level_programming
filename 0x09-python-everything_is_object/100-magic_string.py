#!/usr/bin/python3


def magic_string():
    #this is the magic stfing func
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    #the returning part
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
