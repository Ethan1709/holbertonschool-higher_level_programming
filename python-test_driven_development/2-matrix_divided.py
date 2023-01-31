#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = []
    rounded = []
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int or type(div) is not float:
        raise TypeError('div must be a number')
    for i in range(len(matrix)):
        if type(matrix[i]) is not int or type(matrix[i]) is not float:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        new.append(list(map(lambda x: x / div, matrix[i])))
    rounded = [[round(x, 2) for x in row] for row in new]
    return rounded
