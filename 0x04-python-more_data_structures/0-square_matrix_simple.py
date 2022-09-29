#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = []
    list2 = []
    for n in matrix:
        list1 = [(i * i) for i in n]
        list2 += list1,
    return (list2)
