#!/usr/bin/python3
def uniq_add(my_list=[]):

    uniq_sum = 0
    for a in set(my_list):
        uniq_sum += a
    return (uniq_sum)
