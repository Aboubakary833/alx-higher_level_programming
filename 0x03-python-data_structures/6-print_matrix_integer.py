#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (isinstance(matrix, list)):
        for _list in matrix:
            for i in _list:
                if i != _list[-1]:
                    print("{:d}".format(i), end=" ")
                else:
                    print("{:d}".format(i))
