#!/usr/bin/python3

"""This module defines a function "lookup" that returns the list of available"""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
