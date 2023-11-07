#!/usr/bin/python3

"""Defines text appending function"""


def append_write(filename="", text=""):
    """Appends a text at the end of a UTF8 file

    Args:
        filename (str): name of the file 
        text (str):  text to append
    Returns:
        numbers of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

