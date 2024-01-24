# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:06:31 2024

@author: qhfan
"""

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n//2):
        for j in range(i,n-i-1):
            matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))