#!/usr/bin/python3
"""Text-indentation func"""


def text_indentation(text):
    """Print text with two new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ko = 0

    while ko < len(text) and text[ko] == ' ':
        ko += 1

    #loof for while ko is less than the length of text
    while ko < len(text):
        print(text[ko], end="")
        if text[ko] in ".:?" or text[ko] == "\n":
            if text[ko] in ":.?":
                print("\n")
            ko = ko + 1
            while text[ko] == ' ' and ko < len(text):
                ko = ko + 1
            continue
        ko += 1
