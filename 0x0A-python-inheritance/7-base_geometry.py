#!/usr/bin/python3

"""Defines the base geometry class Base-Geometry"""


class BaseGeometry:
    """Reprsent the base geometry"""

    def area(self):
        """is not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter of an integer

        Args:
            name (str): The name of the parameter
            value (int): The parameter to validate
        Raises:
            TypeError: is value is not an integer
            ValueError: is value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

