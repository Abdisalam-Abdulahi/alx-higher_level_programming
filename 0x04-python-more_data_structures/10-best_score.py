#!/usr/bin/python3

def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.
    """
    maxi = 0
    max_key = ""
    if a_dictionary is None or a_dictionary == { }:
        return None

    for k, v in a_dictionary.items():
        if v > maxi:
            maxi = v
            max_key = k
    return max_key
