#!/usr/bin/python3
def no_c(my_string):
    char_to_remove = 'c'

    for i in my_string:
        if i != char_to_remove and i != char_to_remove.upper():
            new_string += i
    return new_string
