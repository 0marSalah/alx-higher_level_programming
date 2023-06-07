#!/usr/bin/python3


"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character
    #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
