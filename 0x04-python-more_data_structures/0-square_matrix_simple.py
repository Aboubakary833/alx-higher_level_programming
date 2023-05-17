#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def colMap(col):
        return col ** 2
    return list(map(lambda row: list(map(colMap, row)), matrix))
