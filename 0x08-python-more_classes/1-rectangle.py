#!/usr/bin/python3

"""module for Rectangle class."""


class Rectangle:
    """Defines a Rectangle."""
    def __init__(self):
        """Initializes a Rectangle."""
        self.__width = 0
        self.__height = 0

    def width(self):
        """getter for width attribute."""
        return self.__width

    def width(self, value):
        """setter for width attribute."""
        self.__width = value

    def height(self):
        """getter for height attribute."""
        return self.__height

    def height(self, value):
        """setter for height attribute."""
        self.__height = value
