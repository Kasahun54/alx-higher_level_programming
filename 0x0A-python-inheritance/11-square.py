#!/usr/bin/python3

"""Defines the Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent square"""

    def __init__(self, size):
        """Initialize square

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
