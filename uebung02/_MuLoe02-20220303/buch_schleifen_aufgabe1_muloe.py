# -*- coding: utf-8 -*-
# Schleifen - Aufgabe 1

roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_numerals_converter(string):

    # try to convert the single characters to decimal numbers
    decimal = []
    for character in string:
        if character in roman_numerals:
            decimal.append(roman_numerals[character])
        else:
            return None

    # convert the roman numerals to a decimal number
    number = 0
    for current_numeral, next_numeral in zip(decimal, decimal[1:] + [0]):
        if current_numeral < next_numeral:
            number -= current_numeral
        else:
            number += current_numeral
    return number


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    numbers = [
        'MDCCCLXXXV',
        'MCMLV',
        'MCMLXXXV',
        'MMXV',
    ]
    for number in numbers:
        print(number + ': ' + str(roman_numerals_converter(number)))
