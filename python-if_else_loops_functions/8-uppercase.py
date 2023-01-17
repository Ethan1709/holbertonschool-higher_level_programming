#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x >= 97 and x <= 122:
            x = x - 32
        y = chr(x)
        if x == 34 or i == 34:
             print("{}".format(y))
        else:
            print("{}".format(y), end="")
