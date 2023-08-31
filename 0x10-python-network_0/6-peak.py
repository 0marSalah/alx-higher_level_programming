#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    s, e = 0, len(list_of_integers) - 1
    while s <= e:
        m = s + ((e - s) // 2)
        if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            e = m - 1
        elif m < len(list_of_integers) - 1 and list_of_integers[m] < list_of_integers[m + 1]:
            s = m + 1
        else:
            return list_of_integers[m]
