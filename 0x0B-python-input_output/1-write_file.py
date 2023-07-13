#!/usr/bin/python3
"""
Function that that writes a string
to a text file (UTF8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of char.
    :param filename: The name of the file to write.
    :param text: The string to be written to the file.
    :return: The number of characters written to the file.
             Returns -1 on erroe.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
