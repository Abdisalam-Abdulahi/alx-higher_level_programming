#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
     prints a dictionary by ordered keys.
    """
    lis = sorted(list(a_dictionary.keys()))
    for i in range(len(lis)):
        print(f"{lis[i]}: {a_dictionary[lis[i]]}")
