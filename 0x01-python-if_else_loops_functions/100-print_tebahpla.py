#!/usr/bin/python3
num = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - num)), end="")
    num = 32 if num == 0 else 0
