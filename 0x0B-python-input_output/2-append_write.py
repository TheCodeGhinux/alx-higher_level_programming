#!/usr/bin/python3
"""
 Append to a file module
"""


def write_file(filename="", text=""):
    """
    Append a string to a text file (UTF-8) and return
    the number of characters written.
    :args:
        filename: add to this object
        text: string to append
    :return: The number of characters written to the file.
             Returns -1 on erroe.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
