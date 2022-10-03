#!/usr/bin/python3
def best_score(a_dictionary):
    n = 0
    if a_dictionary is None or len(a_dictionary) == 0:
        return
    for i, v in a_dictionary.items():
        if v > n:
            n = v
            c = i
    return (c)
