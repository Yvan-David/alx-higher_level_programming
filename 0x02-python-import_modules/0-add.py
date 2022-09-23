#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add
    add.a = 1
    add.b = 2
    print("{} + {} = {}".format(add.a, add.b, add(add.a, add.b)))
