#!/usr/bin/python3
"""append after func is defined here"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text next to each lines"""
    note = ""

    # opening file
    with open(filename) as newfile:
        for x in newfile:
            note += x
            if search_string in x:
                note += new_string
    # opening file as write mode
    with open(filename, "w") as w:
        w.write(note)
