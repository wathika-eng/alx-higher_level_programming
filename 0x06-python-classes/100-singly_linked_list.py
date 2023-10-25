#!/usr/bin/python3
"""singly linked list in python"""


class Node:
    """ "Make the class Node"""

    def __init__(self, data, next_node=None):
        """Init the class Node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data entity"""

        return self.__data

    @data.setter
    def data(self, value):
        """check data entity"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """move to the next node in list and return it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """what is the next node?"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """class Single linked list"""

    def __init__(self):
        """Init the list"""

        self.head = None

    def __str__(self):
        """Get the list"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """Input data
        Argc:
            value: data to be in the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
        pass
