#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = matrix.copy()

    for n in range(len(matrix)):
        nmatrix[n] = list(map(lambda x: x**2, matrix[n]))

    return (nmatrix)
