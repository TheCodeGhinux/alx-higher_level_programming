#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for a in set_1:
        if a in set_2:
            common_set.add(a)
    return common_set
