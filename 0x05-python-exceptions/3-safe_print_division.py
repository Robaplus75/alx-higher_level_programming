#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        quo = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        quo = None
    finally:
        print("Inside result: {}".format(quo))
    return (quo)
