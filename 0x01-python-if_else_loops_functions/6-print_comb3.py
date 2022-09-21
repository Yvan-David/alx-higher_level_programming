#!/usr/bin/python3
for v in range(0, 10):
    for n in range(0, 10):
        if v != n and v < n:
            if v != 8 or n != 9:
                print("{:d}{:d}".format(v, n), end=", ")
print("89")
