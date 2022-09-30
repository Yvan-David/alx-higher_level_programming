#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list.copy()
    for n in new_list:
        if n == search:
            i = new_list.index(n)
            new_list[i] = replace
    return (new_list)
