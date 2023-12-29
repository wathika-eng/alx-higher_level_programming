#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialize
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Raises:
            TypeError: width and height
            ValueError: width and height
        """
        self.__perimeter = None
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ The height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 0 if self.width == 0 or self.height == 0 else (
            self.width + self.height) * 2
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += "#" * self.width
            if i != self.height - 1:
                rectangle_str += "\n"
        return rectangle_str[::-1]

