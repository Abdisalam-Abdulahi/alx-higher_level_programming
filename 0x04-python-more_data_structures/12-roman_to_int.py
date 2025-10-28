#!/usr/bin/python3

def roman_to_int(roman_string):
    """
     converts a Roman numeral to an integer
    """
    if type(roman_string) is not str or roman_string is None:
        return 0
    special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    basic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for k, v in special.items():
        if k == roman_string:
            return v

    for i in range(len(roman_string)):
        if roman_string[i] in basic:
            if i == (len(roman_string) - 2) and roman_string[len(roman_string) - 2] + roman_string[len(roman_string) - 1] in special:
                sum += special[roman_string[len(roman_string) - 2] + roman_string[len(roman_string) - 1]]  
                return sum
            else:
                sum += basic[roman_string[i]]
    return sum
