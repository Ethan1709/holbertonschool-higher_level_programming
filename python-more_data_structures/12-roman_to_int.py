#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    k = 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i != (len(roman_string) - 1) and r[roman_string[i]] \
                < r[roman_string[i + 1]]:
            k -= r[roman_string[i]]
        else:
            k += r[roman_string[i]]
    return k
