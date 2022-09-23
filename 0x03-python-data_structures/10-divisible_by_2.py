#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    _list = list(my_list)
    for index in _list:
        if index % 2 == 0:
            _list[index] = True
        else:
            _list[index] = False
    return _list
