#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    x = len(matrix)
    y = len(matrix[0])

    for a in range(x):
        row_str = ""
        for b in range(y):
            row += "{:d}".format(matrix[a][b])
            if b != cols - 1:
                row += " "
        print(row)
