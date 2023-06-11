#!/usr/bin/python3


def no_c(my_string):
    """
    A function to remove all characters c and C from a string.
    """
    copy = [p for p in my_string if p != 'c' and p != 'C']
    return ("".join(copy))
