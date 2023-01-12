#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    weight = 0

    for n in my_list:
        number += n[0] * n[1]
        weight += n[1]

    return (number / weight)
