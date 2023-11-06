#!/usr/bin/python3

"""Defines the class MyInt that inherits from int"""


class MyInt(int):
    """Invert the int operators == and !="""

    def __eq__(self, value):
        """Override those == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override those != operator with == behavior"""
        return self.real == value
