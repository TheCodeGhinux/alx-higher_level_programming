#!/usr/bin/python3
def remove_char_at(string, n):
    if abs(n) > len(string):
        return string
    return string[:n] + string[n+1:]
