# 0x08. Python - More Classes and Objects

## Requirements

General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.8.*)
    All your files must be executable
    The length of your files will be tested using wc

---

## 0. Simple rectangle

mandatory

Write an empty class Rectangle that defines a rectangle:

    You are not allowed to import any module

---

## 1. Real definition of a rectangle

mandatory

Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            if width is less than 0, raise a ValueError exception with the message width must be >= 0
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            if height is less than 0, raise a ValueError exception with the message height must be >= 0
    Instantiation with optional width and height: def __init__(self, width=0, height=0):
    You are not allowed to import any module

---

## 2. Area and Perimeter

mandatory

Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            if width is less than 0, raise a ValueError exception with the message width must be >= 0
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            if height is less than 0, raise a ValueError exception with the message height must be >= 0
    Instantiation with optional width and height: def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the rectangle perimeter:
        if width or height is equal to 0, perimeter is equal to 0
    You are not allowed to import any module

---

## 3. String representation

mandatory

Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
            if width is less than 0, raise a ValueError exception with the message width must be >= 0
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
            if height is less than 0, raise a ValueError exception with the message height must be >= 0
    Instantiation with optional width and height: def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the rectangle perimeter:
        if width or height is equal to 0, perimeter has to be equal to 0
    print() and str() should print the rectangle with the character #: (see example below)
        if width or height is equal to 0, return an empty string
    You are not allowed to import any module

    guillaume@ubuntu:~/0x08$ cat 3-main.py
    #!/usr/bin/python3
    Rectangle = __import__('3-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))

    guillaume@ubuntu:~/0x08$ ./3-main.py
    Area: 8 - Perimeter: 12
    ##
    ##
    ##
    ##
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    --
    ##########
    ##########
    ##########
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    guillaume@ubuntu:~/0x08$

---

##

---

##

---

##

---
