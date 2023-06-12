#!/bin/usr/python3
def print_matrix_integer(matrix=[[]]):

    x = len(matrix)

    for a in range(x):
        y = len(matrix[a])
        for b in range(y):
            print("{:d}".format(matrix[a][b]), end="")
            if b != y - 1:
                print(" ", end="")

        print(" ")
