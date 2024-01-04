#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Raises:
            TypeError: width and height
            ValueError: width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle"""
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
        """The height of the rectangle"""
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
        """Return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return (
            0
            if self.width == 0 or self.height == 0
            else ((self.width * 2) + (self.height * 2))
        )

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
