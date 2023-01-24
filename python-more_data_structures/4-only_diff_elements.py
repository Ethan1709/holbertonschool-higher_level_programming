#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)
    c = [x for x in b if x not in a] + [x for x in a if x not in b]
    return c
