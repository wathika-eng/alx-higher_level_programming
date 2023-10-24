#!/usr/bin/python3

"""Define a class Square that defines a square"""


class Square:
    """Make the square"""

    def __init__(self, size=0):
        """Initialize it
        Argc:
            size of square
        """
        if not isinstance(int, size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
