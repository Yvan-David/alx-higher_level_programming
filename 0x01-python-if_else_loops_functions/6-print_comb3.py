#!/usr/bin/python3
for v in range(0, 10):
    for n in range(0, 10):
        if v != 9 and n != 9:
            print("{:d}{:d}".format(v, n), end=", ")
print('99')
