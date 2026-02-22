#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Returns a new matrix.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    # 1. Check if div is a number
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
        
    # 2. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Check if matrix is actually a list and not empty
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(err_msg)

    new_matrix = []
    
    # Get the length of the first row to compare the rest
    if type(matrix[0]) is list:
        row_length = len(matrix[0])
    else:
        raise TypeError(err_msg)

    # 4. Loop through the matrix
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_msg)
            
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
            
        new_row = []
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_msg)
            
            # Divide and round to 2 decimal places
            result = round(item / div, 2)
            new_row.append(result)
            
        new_matrix.append(new_row)

    return new_matrix
