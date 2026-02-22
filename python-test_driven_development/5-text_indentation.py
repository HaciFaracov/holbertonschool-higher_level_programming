#!/usr/bin/python3
"""
This module contains a function that indents text based on punctuation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after punctuation: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = ('.', '?', ':')
    i = 0
    # Requirement: No space at the beginning or end of printed lines
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special:
            print("\n")
            i += 1
            # Skip all spaces following the punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
