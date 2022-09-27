#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    n = 0
    v = 0
    for i in my_list:
        if i < 0:
            v = v + 1
        else:
            break
    if v == len(my_list):
        lis = [(-i) for i in my_list]
        n = lis[0]
        for c in lis:
            if c < n:
                n = c
        return (-n)
    for i in my_list:
        if i > n:
            n = i
    return (n)
