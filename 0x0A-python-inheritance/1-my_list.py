#!/usr/bin/python3

"""This module contain MyList class that inherits from list."""


class MyList(list):
    """Define a MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)."""
        print(sorted(self))
