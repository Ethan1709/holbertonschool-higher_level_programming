#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    i = 0
    for i in range(len(list_a)):
        i += 1
    if i > 2:
        list_a[2:] = []
    if i == 1:
        list_a += [0]
    if i == 0:
        list_a += [0, 0]

    j = 0
    for j in range(0, len(list_b)):
        j += 1
    if j > 2:
        list_b[2:] = []
    if j == 1:
        list_b += [0]
    if j == 0:
        list_b += [0, 0]


    z = zip(list_a, list_b)
    sum = [x + y for (x, y) in z]
    sum = tuple(sum)
    return sum
