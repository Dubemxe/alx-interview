#!/usr/bin/python3
'''
A module that rotates a 2D matrix by 90 degrees
'''


def rotate_2d_matrix(matrix):
    """ Reverses and transpose a n x n matrix """
    n = len(matrix)

    for i in range(n):
        for j in range(int(n/2)):
            temp = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[j][i]
            matrix[j][i] = temp

    """ Transpose the matrix """
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
