#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    new_list = []
    sum = 0
    for n in my_list:
        if n not in new_list:
            sum += n
            new_list.append(n)
    return sum

