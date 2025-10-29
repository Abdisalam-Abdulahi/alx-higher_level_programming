#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers
    """
    try:
        i = 0
        le = 0
        while (i < x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                le += 1
            i += 1
        print()
        return le
    except IndexError:
        raise IndexError("list index out of range")
