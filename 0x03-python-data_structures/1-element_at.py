#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == -idx or idx > len(my_list):
        return (None)
    for i in my_list:
        if my_list.index(i) == idx:
            return (i)
