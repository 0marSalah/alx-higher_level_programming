#!/usr/bin/python3
# a function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        m = left + (left - right) // 2

        if list_of_integers[m] < list_of_integers[m + 1]: left = m + 1
        else: right = m
    return list_of_integers[m]
