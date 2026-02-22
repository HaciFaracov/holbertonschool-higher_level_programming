#!/usr/bin/python3
"""
This module provides a function for text formatting.
It specifically handles indentation and newlines based on punctuation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    There should be no space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters that trigger a double newline
    special = (".", "?", ":")
    i = 0
    # Requirement: No space at the beginning or end of printed lines
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special:
            print()
            print()
            i += 1
            # Skip all spaces immediately following the special character
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
