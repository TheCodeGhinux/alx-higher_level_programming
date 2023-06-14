#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dic = {}
    for key, value in a_dictionary.items():
        mul_dic[key] = value * 2
    return mul_dic
