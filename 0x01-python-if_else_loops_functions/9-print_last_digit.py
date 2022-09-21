#!/usr/bin/python3
def print_last_digit(number):
    if number + 1 is False:
        return
    if number < -1:
        number = -number
    n = number % 10
    print("{}".format(n), end="")
    return n
