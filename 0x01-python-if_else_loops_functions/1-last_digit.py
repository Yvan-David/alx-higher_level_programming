#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numberp = number * -1
else:
    numberp = number
n = numberp % 10
if n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n < 6:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {n} and is greater than 5")