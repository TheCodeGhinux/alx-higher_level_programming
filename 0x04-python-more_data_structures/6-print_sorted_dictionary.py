#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(b, a_dictionary[b])) for b in sorted(a_dictionary)]
