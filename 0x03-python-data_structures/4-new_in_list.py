#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    nu_list = my_list.copy()
    nu_list[idx] = element
    return (nu_list)
