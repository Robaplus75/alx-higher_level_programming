#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg = argv
    n = len(arg) - 1

    if n == 1:
        print("{} argument:".format(n))
    elif n == 0:
        print("{} argument.".format(n))
    else:
        print("{} arguments:".format(n))

    for i in range(1, len(arg)):
        print("{}: {}".format(i, arg[i]))
