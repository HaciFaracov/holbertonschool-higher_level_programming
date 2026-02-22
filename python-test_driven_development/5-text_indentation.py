#!/usr/bin/python3
"""
This module contains a function that indents text based on punctuation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Removes leading and trailing spaces from each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ('.', '?', ':')
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        print(char, end="")
        skip_space = False

        if char in special_chars:
            print("\n")
            skip_space = True
