#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (isinstance(matrix, list)):
        for _list in matrix:
            index = 0
            for i in _list:
                if (index != 2):
                    print("{:d}".format(i), end=" ")
                else:
                    print("{:d}".format(i))
                index += 1
