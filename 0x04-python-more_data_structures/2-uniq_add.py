#!/usr/bin/python3
def search_replace(my_list, search, replace):

    uniq_sum = 0
    for a in set(my_list):
        uniq_sum += a
    return (uniq_sum)
