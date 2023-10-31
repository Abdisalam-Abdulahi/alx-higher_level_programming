#!/usr/bin/python3

"""
function that prints a square with the character #
Prototype: def print_square(size):
size is the size length of the square
You are not allowed to import any module
"""


def print_square(size):
    """
    function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for height in range(size):
        for width in range(size):
            print("#", end="")
        print()
