#!/usr/bin/python3

"""Defin a class Node."""

class Node:
    """Represent a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.
        Args:
            data (int): The data of the new node.
            next_node (Node): The next node of the new node.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return (self.__data)
    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        
    @property
    def next_node(self):
        """Get the next node of the node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        
"""Define a class SinglyLinkedList."""


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize a new singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the singly linked list."""
        string = ""
        node = self.__head
        while node is not None:
            string += str(node.data)
            node = node.next_node
            if node is not None:
                string += "\n"
        return (string)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        node = self.__head
        while node.next_node is not None:
            if value < node.next_node.data:
                break
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
