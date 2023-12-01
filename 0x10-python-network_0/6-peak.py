#!/usr/bin/python3
"""Function that finds a peak in a
  list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Defines a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    int_size = len(list_of_integers)
    if int_size == 1:
        return list_of_integers[0]
    elif int_size == 2:
        return max(list_of_integers)

    mid_size = int(int_size / 2)
    peak = list_of_integers[mid_size]
    if peak > list_of_integers[mid_size - 1] and peak > list_of_integers[mid_size + 1]:
        return peak
    elif peak < list_of_integers[mid_size - 1]:
        return find_peak(list_of_integers[:mid_size])
    else:
        return find_peak(list_of_integers[mid_size + 1:])