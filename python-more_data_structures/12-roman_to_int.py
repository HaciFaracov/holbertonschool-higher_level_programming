#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0

    for i in range(len(roman_string)):
        # If a smaller numeral is before a larger one (like IV or IX), subtract it.
        if i + 1 < len(roman_string) and r_dict[roman_string[i]] < r_dict[roman_string[i + 1]]:
            num -= r_dict[roman_string[i]]
        # Otherwise, add it.
        else:
            num += r_dict[roman_string[i]]

    return num
