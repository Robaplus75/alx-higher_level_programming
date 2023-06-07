#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int((str(number))[-1]) == 0:
    logic = "0"
elif int((str(number))[-1]) > 5:
    logic = "greater than 5"
else:
    logic = "less than 6 and not 0"
print(f"Last digit of {number} is {(str(number))[-1]} and is {logic}")
