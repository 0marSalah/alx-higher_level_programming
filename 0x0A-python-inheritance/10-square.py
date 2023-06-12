#!/usr/bin/python3
"""this module contains a class Square that inherits from Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size):
        """
        Initializes an instance.
        Args:
        size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2


s = Square(13)

print(s)
print(s.area())
