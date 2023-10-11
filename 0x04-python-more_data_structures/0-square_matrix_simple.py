#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mm = matrix.copy()
    for i in range(len(matrix)):
        mm[i] = list(map(lambda x: x**2, matrix[i]))
        return (mm)
