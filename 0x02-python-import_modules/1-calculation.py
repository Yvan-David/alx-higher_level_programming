#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    if (type(a)) == int and (type(b)) == int:
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        print("{:d} / {:d} = {:d}".format(a, b, int(div(a, b))))
