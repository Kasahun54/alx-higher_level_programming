#!/usr/bin/python3
def no_c(my_string):
    char_to_remove = 'c'

    for i in my_string:
        if my_string[i] != 'c' and my_string != 'C':
            new_string += i
    return new_string
