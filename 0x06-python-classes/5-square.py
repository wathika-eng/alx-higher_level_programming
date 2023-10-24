#!/usr/bin/python3

"""Define the class"""


class Square:
    """Make a square"""

    def __init__(self, size):
        """Init the square
        Argc:
            size of square in numeric
        """
        self.size = size

    @property
    def size(self):
        """Size of sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Represent the square with # symbol"""
        for x in range(0, self.__size):
            [print("#", end="") for a in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
