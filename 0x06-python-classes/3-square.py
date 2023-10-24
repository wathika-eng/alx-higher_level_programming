#!/usr/bin/python3

"""Define a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Make the square"""

    def __init__(self, size=0):
        """Init the Square
        Argc:
            size in int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Function to calculate area"""
        return self.__size * self.__size
