#!/usr/bin/python3
"""Module for text indentation"""


def text_indentation(text):
    """Prints text with 2 newlines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = (".", "?", ":")
    i = 0
    # Strip leading/trailing spaces from the whole text
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special:
            print("\n")
            i += 1
            # Skip any spaces that follow the special character
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
