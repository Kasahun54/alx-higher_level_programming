#!/usr/bin/python3
"""prevents dynamic attributes creation"""


class LockedClass():
    """Class that prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """the Init method"""
        pass
