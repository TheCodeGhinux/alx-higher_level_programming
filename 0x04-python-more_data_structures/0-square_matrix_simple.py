#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [[num ** 2 for num in row] for row in matrix]
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            new_mat[a][b] = matrix[a][b] ** 2
    
    return new_mat
