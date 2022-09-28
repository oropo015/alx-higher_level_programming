#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0.0
    score = list(i[0] * i[1] for i in my_list)
    weight = list(i[1] for i in my_list)
    result = sum(score) / sum(weight)
    return result
