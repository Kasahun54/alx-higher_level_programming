#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = ( i for i in my_list()
    length = len(new_list)
    i = 0
    while i < length:
        if new_list[i] % 2 == 0:
            new_list[i] = "True"
        else:
            new_list[i] = "False"
    return new_list
