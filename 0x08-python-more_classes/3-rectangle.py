#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represent the rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the new Rectangle.

        Args:
            width (int): a width of a new rectangle.
            height (int): a height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set a width of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set a height of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return a area of a Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return a perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return a printable representation of a Rectangle.

        Represents a rectangle with a # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

