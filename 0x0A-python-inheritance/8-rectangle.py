#!/usr/bin/python3
"""this module contains a class Rectangle that inherits from BaseGeometry"""


class Rctangle(BaseGeometry):
    """Represents a Rectangle."""

    def __init__(self, width, height):
        """
        Initializes an instance.
        Args:
        width: width of the rectangle
        height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
