#!/usr/bin/python3
"""Module for text indentation"""


def text_indentation(text):
    """Prints text with 2 newlines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = (".", "?", ":")
    s = text.strip(" ")
    i = 0
    while i < len(s):
        print(s[i], end="")
        if s[i] in special:
            print("\n")
            i += 1
            while i < len(s) and s[i] == " ":
                i += 1
            continue
        i += 1
