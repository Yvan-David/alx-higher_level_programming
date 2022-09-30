#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dicio = sorted(a_dictionary)
    for i in dicio:
        for n, v in a_dictionary.items():
            if i == n:
                print('{} : {}'.format(i, v))
