#!/usr/bin/python3

def roman_to_int(roman_string):
    """
     converts a Roman numeral to an integer
    """
    if type(roman_string) is not str or roman_string is None:
        return 0
    special = ["IV", "IX", "XL", "XC", "CD", "CM"]
    basic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range(len(special)):
        if special[i] == roman_string:
            return basic[roman_string[1]] - basic[roman_string[0]]

    for i in roman_string:
        if i in basic:
            sum += basic[i]
    return sum
