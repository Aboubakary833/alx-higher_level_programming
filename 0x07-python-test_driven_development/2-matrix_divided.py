#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divide a matrix elements.
    Args:
        matrix (list): A list of ints and floats lists.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        The result of the division.
    """
    if (matrix == [] or not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(list_element, int) or isinstance(list_element, float))
                for list_element in [row_el for row in matrix for row_el in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
