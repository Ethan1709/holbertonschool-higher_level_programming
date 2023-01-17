#!/usr/bin/python3
def uppercase(str):
    str = chr(str)
    if ord(str) >= ord('A') and ord(str) <= ord('Z'):
        print("{}".format(str))
    else:
        str = ord(str) - 32
        print("{}".format(str))
