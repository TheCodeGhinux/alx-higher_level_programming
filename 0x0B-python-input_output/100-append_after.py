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
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as a:
        a.write(text)
