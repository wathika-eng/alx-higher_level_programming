#!/usr/bin/python3

"""Define a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Make the square"""

    def __init__(self, size=0):
        """Init the square
        Argc:
            size in terms of int
        """
        self.size = size

        @property
        def size(self):
            """Update size of square"""
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """Get area"""
        return self.__size * self.__size

    def __less__(self, other):
        return self.area() <= other.area()

    def __lessthan__(self, other):
        return self.area() < other.area()

    def __great__(self, other):
        return self.area() >= other.area()

    def __noteq__(self, other):
        return self.area() != other.area()

    def __greater__(self, other):
        return self.area() > other.area()

    def __equal__(self, other):
        return self.area() == other.area()
