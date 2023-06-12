#!/usr/bin/python3
"""
  this module defines a class-function checking if an object is an
  instance or inherited instance of a class
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class

    Args:
        obj (unknown): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return (isinstance(obj, a_class))
