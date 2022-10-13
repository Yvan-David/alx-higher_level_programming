#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        v = []
        c = []
        for i in my_list:
            try:
                v.append(i)
                if (my_list.index(i) + 1 == x):
                    raise TypeError
            except TypeError:
                break
        for i in v:
            print("{}".format(i), end='')
        print('')
        if ((v == c) or x == 0):
            raise TypeError
    except TypeError:
        return (0)
    return (v.index(i) + 1)
