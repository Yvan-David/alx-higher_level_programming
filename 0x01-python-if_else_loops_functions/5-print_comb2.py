#!/usr/bin/python3
for v in range(00, 100):
    if v < 10:
        print("0{:d}".format(v), end=", ")
    else:
        print("{}".format((', ' + v and v)if v != 99 else 99),end="")