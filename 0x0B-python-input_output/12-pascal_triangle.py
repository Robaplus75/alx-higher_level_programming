#!/usr/bin/python3
"""Pascal triangle func is defined here"""


def pascal_triangle(n):
    """pascal triangle represetntaion"""
    if n <= 0:
        return []

    tri = [[1]]
    # The loop begins here
    while len(tri) != n:
        ir = tri[-1]

        temporary = [1]
        #another loop here
        for i in range(len(tri) - 1):
            temporary.append(ir[i] + ir[i + 1])
        #appending process
        temporary.append(1)

        tri.append(temporary)
    return tri
