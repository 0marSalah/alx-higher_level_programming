#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry():
    """Represents a BaseGeometry."""

    def area(self):
        """function that raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
