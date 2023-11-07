#!/usr/bin/python3

"""Defines writing to JSON file function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

