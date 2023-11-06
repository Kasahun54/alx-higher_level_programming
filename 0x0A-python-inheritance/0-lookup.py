#!/usr/bin/python3

"""Defines a lookup function."""


def lookup(obj):
    """Return a list of attributes and methods available attributes."""
    return (dir(obj))
