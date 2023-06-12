#!/bin/usr/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    y = len(matrix[0])

    for a in range(x):
        for b in range(y):
            print("{:d}".format(matrix[a][b]), end="")
            if b != y - 1:
                print(" ", end="")

        print(" ")
