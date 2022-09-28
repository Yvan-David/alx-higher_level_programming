#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis2 = [False for i in my_list]
    for i in my_list:
        if i % 2 == 0:
            lis2[my_list.index(i)] = True
    return (lis2)
