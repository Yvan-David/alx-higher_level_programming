#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for n in i:
            print("{}".format(n), end="")
        print("")
