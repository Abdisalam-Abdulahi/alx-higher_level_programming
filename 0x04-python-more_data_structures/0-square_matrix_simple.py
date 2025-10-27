#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix.
    """
    new = []
    for i in range(len(matrix)):
        inner = []
        for k in range(len(matrix[i])):
            inner.append(matrix[i][k] ** 2)
        new.append(inner)

    return new
