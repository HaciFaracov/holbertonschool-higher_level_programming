#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It provides a way to represent rectangles with validated dimensions.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle using BaseGeometry as a parent.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with validated dimensions.

        Args:
            width (int): The horizontal dimension.
            height (int): The vertical dimension.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
