#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
      Raises:
        TypeError: If a or b is not an integer or float.
      Returns:
        The sum of a and b.
      Args:
        a (int): The first parameter.
        b (int): The second parameter.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
