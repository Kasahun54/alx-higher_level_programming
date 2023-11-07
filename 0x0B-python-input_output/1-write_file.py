#!/usr/bin/python3

"""Defines text writing function"""


def write_file(filename="", text=""):
    """Write a text to a UTF8 file

    Args:
        filename (str): name of the file 
        text (str): text to write 
    Returns:
        The number of characters written in the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

