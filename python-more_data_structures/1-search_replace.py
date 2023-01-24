#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new = []
    for i in range(1, len(my_list)):
        if i == search:
            new.append(replace)
        else:
            new.append(my_list[i])
    return new
