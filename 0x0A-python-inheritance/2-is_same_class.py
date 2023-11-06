#!/usr/bin/python3

"""Defines the class-checking fun"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class

    Args:
        obj (any): The object to be check
        a_class (type): class  match the type of obj to
    Returns:
        If obj is exactly an instance of a_class - True
        or - False
    """
    if type(obj) == a_class:
        return True
    return False
