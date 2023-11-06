#!/usr/bin/python3

"""Defines class MyList and inherited list"""


class MyList(list):
    """sorted printing"""

    def print_sorted(self):
        """sorted in ascending order"""
        print(sorted(self))
