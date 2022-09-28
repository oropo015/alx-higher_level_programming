#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    r_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    temp = list(roman_string)
    if len(temp) > 1:
        x = 0
        for i in temp:
            try:
                if temp[x] == 'I' and temp[x + 1] == 'V':
                    temp[x:x + 2] = [''.join(temp[x:x + 2])]
            except IndexError:
                pass
            try:
                if temp[x] == 'I' and temp[x + 1] == 'X':
                    temp[x:x + 2] = [''.join(temp[x:x + 2])]
            except IndexError:
                pass
            x += 1
    for k, v in r_dict.items():
        for index in temp:
            if index == k:
                result += v
    return result
