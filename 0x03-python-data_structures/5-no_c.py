#!/usr/bin/env python3

def no_c(my_string):
    """
    removes all characters c and C from a string
    """
    new_str = my_string
    new_str = "".join([i for i in new_str if i != 'C' and i != 'c'])
    return new_str
