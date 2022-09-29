#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list.copy()
    if search in new_list:
        i = new_list.index(search)
        new_list[i] = replace
    return (new_list)