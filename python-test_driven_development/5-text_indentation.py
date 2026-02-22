#!/usr/bin/python3
"""Module for text indentation"""


def text_indentation(text):
    """Prints text with 2 newlines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = (".", "?", ":")
    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special:
            print()
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
