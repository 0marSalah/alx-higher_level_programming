#!/usr/bin/python3

"""module for Rectangle class."""


class Rectangle:
    """Defines a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle."""
        self.__width = width
        self.__height = height

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


my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
