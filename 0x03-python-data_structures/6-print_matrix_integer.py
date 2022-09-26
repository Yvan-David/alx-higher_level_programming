#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            print((matrix[i])[n],end=' ' if n != (len(matrix[i]) - 1) else '')
        print(end='\n')