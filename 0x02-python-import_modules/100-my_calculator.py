#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import mul, sub, add, div

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, ops[argv[2]](a, b)))
