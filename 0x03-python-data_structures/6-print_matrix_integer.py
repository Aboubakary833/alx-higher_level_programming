#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (isinstance(matrix, list)):
        for _list in matrix:
            for i in _list:
                print("{:d}".format(i), end=" " if i != _list[-1] else "")
            print()
