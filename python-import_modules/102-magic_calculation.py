#!/usr/bin/python3
import dis
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        return
    c = add(a, b)
    for i in range(4, 6):
            c = add(c ,i)
    return sub(a, b)
dis.dis(magic_calculation)
