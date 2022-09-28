#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    i = 0
    for key, value in a_dictionary.items():
        if value > i:
            i = value
    for key, value in a_dictionary.items():
        if value == i:
            return key
