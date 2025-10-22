#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list.
    """
    if idx < len(my_list) and idx > 0:
        del my_list[idx]
    return my_list
