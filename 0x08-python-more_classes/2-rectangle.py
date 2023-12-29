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
        if self.width or self.height == 0:
            self.__perimeter = 0
        return self.width + self.height
