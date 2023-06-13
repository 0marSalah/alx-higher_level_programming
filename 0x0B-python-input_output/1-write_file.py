#!/usr/bin/python3
"""
    this module contains a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
