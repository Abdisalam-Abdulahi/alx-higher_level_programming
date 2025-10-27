#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique integers in a list
    """
    my_list = list(set(my_list))
    sum = 0

    for i in range(len(my_list)):
        sum += my_list[i]

    return sum
