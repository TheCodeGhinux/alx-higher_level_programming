#!/usr/bin/python3
def no_c(my_string):
    string = ''
    for str in my_string:
        if str != 'c' and str != 'C':
            string += str
    return string
