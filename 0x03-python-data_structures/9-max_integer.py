#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    if my_list == "":
        return None
    else:
        for i in range(len(my_list)):
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
        return temp
