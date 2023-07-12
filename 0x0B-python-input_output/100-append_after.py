#!/usr/bin/python3
"""
Function that inserts a line of
text to a file, after each
line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """To insert text after each
    line with a given string.
    """
    text = ""
    with open(filename) as f:
        for l in f:
            text += l
            if search_string in l:
                text += new_string
    with open(filename, "w") as a:
        a.write(text)
