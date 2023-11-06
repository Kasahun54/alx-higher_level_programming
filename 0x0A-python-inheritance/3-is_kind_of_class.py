#!/usr/bin/python3

"""Defines the class and inherited class checking function."""


def is_kind_of_class(obj, a_class):
    """Check inherited instance of a class

    Args:
        obj (any): the object to be check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is inherited instance of a_class - True.
        or - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
