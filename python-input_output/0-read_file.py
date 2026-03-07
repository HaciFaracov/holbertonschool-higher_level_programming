#!/usr/bin/python3
"""
This module contains a function that reads a text file.
The function prints the content of a UTF-8 encoded text file to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
