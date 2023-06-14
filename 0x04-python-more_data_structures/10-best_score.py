#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    a = None
    b = float('-inf')
    for key, value in a_dictionary.items():
        if value > b:
            a = key
            b = value

    return a
