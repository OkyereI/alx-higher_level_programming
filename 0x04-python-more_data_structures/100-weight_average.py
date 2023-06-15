#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    A function that returns the weighted
    average of all integers tuple
    """
    weighted_avg = 0
    size = 0
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    for tuple in my_list:
        weighted_avg += (tuple[0] * tuple[1])
        size += tuple[1]
    return (weighted_avg / size)

