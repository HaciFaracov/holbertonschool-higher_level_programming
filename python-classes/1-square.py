#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes the square with a specific size.

        Args:
            size: The size of the square (no type/value validation yet).
        """
        self.__size = size
