#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new = my_list[:]
    if idx < 0:
        return new
    if idx not in range(len(my_list)):
        return new
    new[idx] = element
    return new
