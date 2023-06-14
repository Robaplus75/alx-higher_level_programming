#!/usr/bin/python3

def no_c(my_string):
    return my_string.translate({ord(j): None for j in 'cC'})
