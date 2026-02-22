#!/usr/bin/python3
"""Module for text indentation"""


def text_indentation(text):
    """Prints text with 2 newlines after punctuation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = (".", "?", ":")
    i = 0
    # Requirement: No space at the beginning or end of printed lines
    text = text.strip()
    while i < len(text):
        print(text[i], end="")
        if text[i] in special:
            # This prints exactly two newlines (one blank line)
            print("\n", end="")
            i += 1
            # Skip all spaces following the punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
