#!/usr/bin/python3

"""Defines a Python class in JSON function."""


def class_to_json(obj):
    """Return the dictionary representation of a data structure."""
    return obj.__dict__

