#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add as c
    c.a = 1
    c.b = 2
    print("{} + {} = {}".format(c.a, c.b, c(c.a, c.b)))
