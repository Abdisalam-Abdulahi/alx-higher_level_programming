#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    finds all multiples of 2 in a list
    """
    new_li = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_li.append(True)
        else:
            new_li.append(False)
    return new_li
