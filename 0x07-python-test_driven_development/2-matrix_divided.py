#!usr/bin/python3

"""module for matrix_divided function."""


def matrix_divided(matrix, div):
    """
      Divides all elements of a matrix.
      Args:
        matrix (list): The matrix to be divided.
        div (int/float): The divisor.
      Raises:
        TypeError: If matrix contains non-int/float.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    new_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return (new_matrix)
