#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x >= 97 and x <= 122:
            x = x - 32
        y = chr(x)
        if i == len(str):
            print("{}".format(y))
        else:
            print("{}".format(y), end='')
