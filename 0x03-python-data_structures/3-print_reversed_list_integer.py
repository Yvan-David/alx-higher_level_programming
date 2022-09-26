#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if len(my_list) != 0:
        for i in range(len(my_list)):
            print("{}".format(my_list[i]))

