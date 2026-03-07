#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists representing the triangle, or empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Start the new row with a 1
        row = [1]
        # Get the previous row
        prev_row = triangle[i - 1]

        # Calculate the middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # End the row with a 1
        row.append(1)
        triangle.append(row)

    return triangle
