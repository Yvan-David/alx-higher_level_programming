#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        v = []
        c = []
        n = 0
        for i in my_list:
            try:
                v.append(i)
                if (my_list.index(i) + 1 == x):
                    raise TypeError
            except TypeError:
                break
        for i in v:
            try:
                i + 1
                print("{}".format(i), end='')
                n = n + 1
            except (TypeError, ValueError):
                continue
        print(''.format())
        if ((v == c) or x == 0):
            raise TypeError
    except TypeError:
        return (0)
    return (n)
