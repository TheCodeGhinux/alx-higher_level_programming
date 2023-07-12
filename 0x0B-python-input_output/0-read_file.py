#!/usr/bin/python3
"""
Function that defines
a text file-reader.
"""


def read_file(filename=""):
    """to print the UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
