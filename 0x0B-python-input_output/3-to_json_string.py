#!/usr/bin/python3

"""Defines the string to JSON converting function"""
import json


def to_json_string(my_obj):
    """Return the JSON representation"""
    return json.dumps(my_obj)

