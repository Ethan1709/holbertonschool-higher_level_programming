#!/usr/bin/env python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n:
            print(" ", end="")
        else:
            print(str[i], end="")
