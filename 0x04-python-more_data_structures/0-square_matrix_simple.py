#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return list(map(
        lambda numlist: list(
            map(lambda num: num * num, numlist)
            ), matrix
        ))
