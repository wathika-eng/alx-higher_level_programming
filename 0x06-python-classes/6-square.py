#!/usr/bin/python3

"""Make the class Square."""


class Square:
    """The class square."""

    def __init__(self, size=0, position=(0, 0)):
        """Init the square.
        Argc:
            size of square in ints
            position of the square in ints
        """
        self.position = position
        self.size = size

    @property
    def size(self):
        """Size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Where is the square at?"""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area"""
        return self.__size * self.__size

    def my_print(self):
        """# to show the square"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
