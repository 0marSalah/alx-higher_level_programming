#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(nums):
    """Finds a peak in nums"""

    s, e = 0, len(nums) - 1
    while s <= e:
        m = s + ((e - s) // 2)
        if m > 0 and nums[m] < nums[m - 1]:
            e = m - 1
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            s = m + 1
        else:
            return nums[m]
