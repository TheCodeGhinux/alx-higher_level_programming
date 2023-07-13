#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """function that returns a list 
    of lists of integers representing 
    the Pascal’s triangle of n
    args:
        n: value
    return
        list
    """
    int_list = []
    if n <= 0:
        return int_list
    for i in range(n):
        num = 11**i
        li = [int(n) for n in str(num)]
        int_list.append(li)
    return int_list
