#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns a tuple with the len of a str and its first chr
    """
    length = len(sentence)
    if length > 0:
        first_chr = sentence[0]
    else:
        first_chr = None
    return (length, first_chr)
